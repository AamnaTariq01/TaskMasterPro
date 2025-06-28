// Main JavaScript file for Todo List Application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize feather icons
    if (typeof feather !== 'undefined') {
        feather.replace();
    }
    
    // Auto-hide flash messages after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Form validation enhancement
    const forms = document.querySelectorAll('form[novalidate]');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
    
    // Auto-submit filter form on change
    const filterForm = document.querySelector('form[action*="index"]');
    if (filterForm) {
        const filterInputs = filterForm.querySelectorAll('select, input[type="search"]');
        let debounceTimer;
        
        filterInputs.forEach(function(input) {
            input.addEventListener('change', function() {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(function() {
                    filterForm.submit();
                }, 300);
            });
            
            // For search input, also listen to keyup with debounce
            if (input.type === 'search' || input.name === 'search') {
                input.addEventListener('keyup', function() {
                    clearTimeout(debounceTimer);
                    debounceTimer = setTimeout(function() {
                        filterForm.submit();
                    }, 500);
                });
            }
        });
    }
    
    // Confirm dialogs for dangerous actions
    const deleteButtons = document.querySelectorAll('button[type="submit"]');
    deleteButtons.forEach(function(button) {
        if (button.textContent.includes('Delete') || button.querySelector('i[data-feather="trash-2"]')) {
            button.addEventListener('click', function(event) {
                const confirmMessage = 'Are you sure you want to delete this task? This action cannot be undone.';
                if (!confirm(confirmMessage)) {
                    event.preventDefault();
                }
            });
        }
    });
    
    // Task completion toggle with visual feedback
    const toggleForms = document.querySelectorAll('.task-toggle-form');
    toggleForms.forEach(function(form) {
        const checkbox = form.querySelector('.task-checkbox');
        if (checkbox) {
            checkbox.addEventListener('change', function() {
                // Add visual feedback
                checkbox.disabled = true;
                const formCheck = checkbox.closest('.form-check');
                formCheck.style.opacity = '0.6';
                
                // Submit form
                form.submit();
            });
        }
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(event) {
        // Ctrl/Cmd + N to add new task
        if ((event.ctrlKey || event.metaKey) && event.key === 'n') {
            event.preventDefault();
            const addTaskLink = document.querySelector('a[href*="add"]');
            if (addTaskLink) {
                addTaskLink.click();
            }
        }
        
        // Escape key to cancel forms
        if (event.key === 'Escape') {
            const cancelButton = document.querySelector('a.btn-secondary');
            if (cancelButton && cancelButton.textContent.includes('Cancel')) {
                cancelButton.click();
            }
        }
    });
    
    // Responsive table handling
    function handleResponsiveElements() {
        const width = window.innerWidth;
        const taskCards = document.querySelectorAll('.card .row.align-items-center');
        
        taskCards.forEach(function(row) {
            if (width < 768) {
                row.classList.remove('align-items-center');
                row.classList.add('align-items-start');
            } else {
                row.classList.add('align-items-center');
                row.classList.remove('align-items-start');
            }
        });
    }
    
    // Handle window resize
    window.addEventListener('resize', handleResponsiveElements);
    handleResponsiveElements(); // Initial call
    
    // Focus management for accessibility
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('search')) {
        const searchInput = document.querySelector('input[name="search"]');
        if (searchInput) {
            searchInput.focus();
        }
    }
    
    // Form auto-save functionality (for edit forms)
    const editForms = document.querySelectorAll('form[action*="edit"]');
    editForms.forEach(function(form) {
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(function(input) {
            input.addEventListener('change', function() {
                // Save to localStorage as backup
                const formData = new FormData(form);
                const data = {};
                for (let [key, value] of formData.entries()) {
                    data[key] = value;
                }
                localStorage.setItem('editFormBackup', JSON.stringify(data));
            });
        });
        
        // Restore from localStorage on page load
        const backup = localStorage.getItem('editFormBackup');
        if (backup) {
            try {
                const data = JSON.parse(backup);
                Object.keys(data).forEach(function(key) {
                    const input = form.querySelector(`[name="${key}"]`);
                    if (input && input.type !== 'hidden') {
                        if (input.type === 'checkbox') {
                            input.checked = data[key] === 'y';
                        } else {
                            input.value = data[key];
                        }
                    }
                });
            } catch (e) {
                console.log('Could not restore form backup');
            }
        }
        
        // Clear backup on successful submission
        form.addEventListener('submit', function() {
            localStorage.removeItem('editFormBackup');
        });
    });
    
    // Performance optimization: Lazy load feather icons
    const observerOptions = {
        root: null,
        rootMargin: '50px',
        threshold: 0.1
    };
    
    const iconObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const icon = entry.target;
                if (icon.hasAttribute('data-feather') && typeof feather !== 'undefined') {
                    feather.replace();
                    iconObserver.unobserve(icon);
                }
            }
        });
    }, observerOptions);
    
    // Observe all feather icons
    document.querySelectorAll('[data-feather]').forEach(function(icon) {
        iconObserver.observe(icon);
    });
});

// Utility functions
function showToast(message, type = 'info') {
    // Create toast element if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
        document.body.appendChild(toastContainer);
    }
    
    const toastEl = document.createElement('div');
    toastEl.className = `toast align-items-center text-white bg-${type} border-0`;
    toastEl.setAttribute('role', 'alert');
    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    toastContainer.appendChild(toastEl);
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
    
    // Remove element after hiding
    toastEl.addEventListener('hidden.bs.toast', function() {
        toastEl.remove();
    });
}

// Export for global access
window.TodoApp = {
    showToast: showToast
};

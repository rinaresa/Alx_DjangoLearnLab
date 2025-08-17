document.addEventListener('DOMContentLoaded', function() {
    // Initialize tag input if Tagify is used
    if (typeof Tagify !== 'undefined') {
        new Tagify(document.querySelector('[data-tagify]'));
    }
});
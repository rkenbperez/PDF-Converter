// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('dropzone-file');
    const submitBtn = document.getElementById('submit-btn');
    const fileDisplay = document.getElementById('file-display');
    const fileList = document.getElementById('file-list');
    const form = document.querySelector('form');

    // Debug: Check if elements exist
    console.log('File input:', fileInput);
    console.log('Submit button:', submitBtn);
    console.log('Form:', form);

    if (!fileInput || !submitBtn || !form) {
        console.error('Missing required elements!');
        return;
    }

    fileInput.addEventListener('change', function() {
        const files = this.files;
        console.log('Files selected:', files.length);
        
        if (files.length > 0) {
            // Show submit button
            submitBtn.classList.remove('hidden');
            console.log('Submit button shown');
            
            // Show file list
            if (fileDisplay && fileList) {
                fileDisplay.classList.remove('hidden');
                
                // Clear previous files
                fileList.innerHTML = '';
                
                // Display selected files
                for (let i = 0; i < files.length; i++) {
                    console.log(`File ${i}: ${files[i].name}`);
                    const fileDiv = document.createElement('div');
                    fileDiv.className = 'bg-gray-100 p-2 mb-2 rounded';
                    fileDiv.textContent = files[i].name;
                    fileList.appendChild(fileDiv);
                }
            }
        } else {
            submitBtn.classList.add('hidden');
            if (fileDisplay) fileDisplay.classList.add('hidden');
        }
    });

    // Add form submission handler for debugging
    form.addEventListener('submit', function(e) {
        console.log('Form submission started!');
        const files = fileInput.files;
        
        if (files.length === 0) {
            console.log('No files selected, preventing submission');
            e.preventDefault();
            alert('Please select files first!');
            return false;
        }
        
        console.log('Submitting form with files:', files.length);
        for (let i = 0; i < files.length; i++) {
            console.log(`Submitting file ${i}: ${files[i].name}, Size: ${files[i].size} bytes`);
        }
        
        // Show loading message
        submitBtn.innerHTML = '⏳ Converting...';
        submitBtn.disabled = true;
    });

    // Add click handler for submit button (additional debugging)
    submitBtn.addEventListener('click', function(e) {
        console.log('Submit button clicked!');
    });
});
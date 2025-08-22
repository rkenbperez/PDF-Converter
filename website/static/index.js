// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('dropzone-file');
    const submitBtn = document.getElementById('submit-btn');
    const fileDisplay = document.getElementById('file-display');
    const fileList = document.getElementById('file-list');

    fileInput.addEventListener('change', function() {
        const files = this.files;
        
        if (files.length > 0) {
            // Show submit button
            submitBtn.classList.remove('hidden');
            
            // Show file list
            fileDisplay.classList.remove('hidden');
            
            // Clear previous files
            fileList.innerHTML = '';
            
            // Display selected files
            for (let i = 0; i < files.length; i++) {
                const fileDiv = document.createElement('div');
                fileDiv.className = 'bg-gray-100 p-2 mb-2 rounded';
                fileDiv.textContent = files[i].name;
                fileList.appendChild(fileDiv);
            }
        } else {
            submitBtn.classList.add('hidden');
            fileDisplay.classList.add('hidden');
        }
    });
});
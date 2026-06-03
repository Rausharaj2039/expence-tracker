/* Modal Logic */
document.addEventListener('DOMContentLoaded', () => {
    const openBtn = document.getElementById('how-it-works-btn');
    const modal = document.getElementById('video-modal');
    const closeBtn = document.getElementById('close-modal');
    const video = document.getElementById('modal-video');

    if (openBtn && modal && closeBtn && video) {
        openBtn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.style.display = 'flex';
        });

        const closeModal = () => {
            modal.style.display = 'none';
            // Reset iframe src to stop video playback
            const currentSrc = video.src;
            video.src = '';
            video.src = currentSrc;
        };

        closeBtn.addEventListener('click', closeModal);

        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal();
            }
        });
    }
});

window.onload=function(){
    const openModalButtons = document.querySelectorAll('[data-modal-target]')
    const closeModalButtons = document.querySelectorAll('[data-close-button]')
    const addTargetButtons = document.querySelectorAll('[data-add-target]')
    const overlay = document.getElementById('overlay')

    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = document.getElementById(button.dataset.modalTarget)
            openModal(modal)
        })
    })

    overlay.addEventListener('click', () => {
        closeAllModal()
    })

    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal')
            closeModal(modal)
        })
    })

    addTargetButtons.forEach(button => {
        button.addEventListener('click', () => {
            const target = document.querySelector(button.dataset.addTarget)
            addToWatchlist(target)
        })
    })

    function openModal(modal) {
        if (modal == null) return
        modal.classList.add('active')
        overlay.classList.add('active')
    }

    function closeModal(modal) {
        if (modal == null) return
        modal.classList.remove('active')
        overlay.classList.remove('active')
    }

    function addToWatchlist(target) {
        if (target == null) return
        closeAllModal()
        href="{% url 'add_to_watchlist' movie.id %}"
    }

    function closeAllModal() {
        const modals = document.querySelectorAll('.modal.active')
        modals.forEach(modal => {
            closeModal(modal)
        })
    }
}

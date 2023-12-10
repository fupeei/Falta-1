var eventos = document.querySelectorAll('.eventos')

eventos.forEach(function(evento) {
    evento.addEventListener('mouseover', function() {
        this.style.transform = 'translate(-5px)';
    });

    evento.addEventListener('mouseout', function() {
        this.style.transform = 'none';
    });
});

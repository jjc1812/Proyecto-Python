document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('formulario');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
 
        if (validateForm()) {
        form.submit();
      }
    });

    function validateForm() {
        const nombre = document.getElementById('nombre').value;
        const DNI = document.getElementById('DNI').value;
        const monto = document.getElementById('monto').value;
        const CBU = document.getElementById('CBU').value;
    
        if (nombre.trim() === '') {
            document.getElementById('nombre').className = "error";
            return false;
        } else {
            document.getElementById('nombre').className = "";
        }
    
        if (DNI.length < 7) {
            alert('Ingrese un número de documento válido con 7 digitos como minimo.');
            return false;
        }
    
        if (monto <= 0) {
            alert('Ingrese un monto mayor a 0.');
            return false;
        }
    
        if (CBU.length < 12) {
            alert('Ingrese su CBU o ALIAS válido con 12 caracteres como minimo.');
            return false;
        }
    
        return true;
    }
});

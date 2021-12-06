 window.addEventListener('scroll', 
        function(){
            var tophead = document.querySelector('.header-container');
            tophead.classList.toggle('fixed', window.scrollY >= 100);
        });
        document.getElementById("navigate").addEventListener('click',
            function(){
                var thenav = document.querySelector(".side-nav");
                thenav.classList.toggle('appear')
            })
            document.getElementById("closer").addEventListener('click',
            function(){
                var thenav = document.querySelector(".side-nav");
                thenav.classList.remove('appear')
            
            })
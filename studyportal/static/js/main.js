// classList - shows/gets all classes
// contains - checks classList for specific class
// add - add class
// remove - remove class
// toggle - toggle class



let navToggle = document.querySelector(".nav-toggle");
let links = document.querySelector(".links");


navToggle.addEventListener("click", () => {
    // console.log(links.classList);
    // console.log(links.classList.contains('links'));

    // Another approach

    // if(links.classList.contains('show-links')){
    //     links.classList.remove('show-links')
    // }
    // else{
    //     links.classList.add("show-links");
    // }

    // One liner

    links.classList.toggle("show-links");
});


// <body>
// <nav className="navbar-dark bg-dark">
//     <div className="nav-center">
//         <!-- Nav Header -->
//         <div className="nav-header">
//             <a className="navbar-brand" href="/">Students Study Portal</a>
//             <button className="nav-toggle">
//                 <i className="fas fa-bars"></i>
//             </button>
//         </div>
//         <!-- links -->
//         <ul className="links ">
//             <li className="nav-item">
//                 <a className="nav-link active" aria-current="page" href="/">Home</a>
//             </li>
//             <li className="nav-item dropdown">
//                 <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
//                    data-toggle="dropdown"
//                    aria-haspopup="true" aria-expanded="false">
//                     Options
//                 </a>
//                 <div className="dropdown-menu" aria-labelledby="navbarDropdown">
//                     <a className="dropdown-item" href="#">Books</a>
//                     <a className="dropdown-item" href="#">Wikipedia</a>
//                     <div className="dropdown-divider"></div>
//
//                     <a className="dropdown-item" href="#">Dictionary</a>
//                     <a className="dropdown-item" href="#">Youtube</a>
//                     <div className="dropdown-divider"></div>
//                     <a className="dropdown-item" href="#">To-do</a>
//                     <a className="dropdown-item" href="#">Notes</a>
//                     <div className="dropdown-divider"></div>
//                 </div>
//             </li>
//             <li className="nav-item">
//                 <a className="nav-link" href="/register">Register</a>
//             </li>
//             <li className="nav-item">
//                 <a className="nav-link" href="/login">Login</a>
//             </li>
//             <li className="nav-item">
//                 <a className="nav-link" href="/logout">Logout</a>
//             </li>
//         </ul>
//         <!-- social media -->
//         <ul className="social-icons">
//             <li>
//                 <a href="https://www.twitter.com">
//                     <i className="fab fa-facebook"></i>
//                 </a>
//             </li>
//             <li>
//                 <a href="https://www.twitter.com">
//                     <i className="fab fa-twitter"></i>
//                 </a>
//             </li>
//             <li>
//                 <a href="https://www.twitter.com">
//                     <i className="fab fa-behance"></i>
//                 </a>
//             </li>
//             <li>
//                 <a href="https://www.twitter.com">
//                     <i className="fab fa-linkedin"></i>
//                 </a>
//             </li>
//             <li>
//                 <a href="https://www.twitter.com">
//                     <i className="fab fa-sketch"></i>
//                 </a>
//             </li>
//         </ul>
//     </div>
// </nav>
// <main>
//
//     {% block body %}
//
//
//     {% endblock %}
//
// </main>
// <!-- javascript -->
// <script src="{% static " js/main.js" %}"></script>
// <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
// <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
//         integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossOrigin="anonymous">
// </script>
// <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
//         integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossOrigin="anonymous">
// </script>
// </body>
















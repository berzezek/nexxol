<template lang="">
  <div>
    <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container px-4 px-lg-5">
        <a class="navbar-brand" href="#page-top"><img class="navbar-logo-img" src="@/assets/img/logo.png"
            style="width: 150px" alt="NEXXOL" /></a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          Меню
          <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="#about">О нас</a></li>
            <li class="nav-item"><a class="nav-link" href="#projects">Проекты</a></li>
            <li class="nav-item"><a class="nav-link" href="#signup">Контакты</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  // methods: {
  //   colapseNav() {
  //     window.addEventListener("DOMContentLoaded", (event) => {
  //       // Navbar shrink function
  //       var navbarShrink = function () {
  //         const navbarCollapsible = document.body.querySelector("#mainNav");
  //         if (!navbarCollapsible) {
  //           return;
  //         }
  //         if (window.scrollY === 0) {
  //           navbarCollapsible.classList.remove("navbar-shrink");
  //         } else {
  //           navbarCollapsible.classList.add("navbar-shrink");
  //         }
  //       };

  //       // Shrink the navbar
  //       navbarShrink();

  //       // Shrink the navbar when page is scrolled
  //       document.addEventListener("scroll", navbarShrink);

  //       // Activate Bootstrap scrollspy on the main nav element
  //       const mainNav = document.body.querySelector("#mainNav");
  //       if (mainNav) {
  //         new bootstrap.ScrollSpy(document.body, {
  //           target: "#mainNav",
  //           offset: 74,
  //         });
  //       }

  //       // Collapse responsive navbar when toggler is visible
  //       const navbarToggler = document.body.querySelector(".navbar-toggler");
  //       const responsiveNavItems = [].slice.call(
  //         document.querySelectorAll("#navbarResponsive .nav-link")
  //       );
  //       responsiveNavItems.map(function (responsiveNavItem) {
  //         responsiveNavItem.addEventListener("click", () => {
  //           if (window.getComputedStyle(navbarToggler).display !== "none") {
  //             navbarToggler.click();
  //           }
  //         });
  //       });
  //     });
  //   },
  // },
  // mounted() {
  //   this.colapseNav()
  // }
};
</script>

<style lang="">
  /* @import '@/css/styles.css' */
</style>
<template>
  <div>
   <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#page-top"><img class="navbar-logo-img" src="../../assets/img/logo.png" style="width: 100px" /></a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
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
        <!-- Masthead-->
        <header class="masthead">
            <div class="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center">
                <div class="d-flex justify-content-center">
                    <div class="text-center">
                        <h1 class="mx-auto my-0 text-uppercase">engine <br/> oil <br/> industrial</h1>
                        <h2 class="text-white-50 mx-auto mt-2 mb-5">Моторные масла в Узбекистане.</h2>
                        <!-- <a class="btn btn-primary" href="#about">Get Started</a> -->
                    </div>
                </div>
            </div>
        </header>
        <!-- About-->
        <section class="about-section text-center" id="about">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-lg-8">
                        <h2 class="text-white mb-4">Наш девиз</h2>
                        <p class="text-white-50">
                            Здесь будет описание о нас. <br/>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia odit distinctio dolores mollitia a aliquam, blanditiis aspernatur perspiciatis, ut unde quibusdam! Necessitatibus numquam dolores delectus ad, perferendis consectetur modi quisquam?
                        </p>
                    </div>
                </div>
                <img class="img-fluid mb-5" src="../../assets/img/xx.png" alt="..." />
            </div>
        </section>
        <!-- Projects-->
        <section class="projects-section bg-light" id="projects">
            <div class="container px-4 px-lg-5">
                <!-- Featured Project Row-->
                <div class="row gx-0 mb-4 mb-lg-5 align-items-center">
                    <div class="col-xl-8 col-lg-7"><img class="img-fluid mb-3 mb-lg-0" src="../../assets/img/oil-shop.webp" alt="..." /></div>
                    <div class="col-xl-4 col-lg-5">
                        <div class="featured-text text-center text-lg-left">
                            <h4 class="text-uppercase">магазин</h4>
                            <p class="text-black-50 mb-0">Что нибудь к описанию <br /> Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores suscipit laudantium at ratione natus? Reiciendis dolor natus voluptas asperiores non, optio sunt, obcaecati porro voluptatibus ut ullam, accusamus unde deleniti!</p>
                        </div>
                    </div>
                </div>
                <!-- Project One Row-->
                <div class="row gx-0 mb-5 mb-lg-0 justify-content-center">
                    <div class="col-lg-6"><img class="img-fluid" src="../../assets/img/1.webp" alt="..." /></div>
                    <div class="col-lg-6">
                        <div class="bg-black text-center h-100 project">
                            <div class="d-flex h-100">
                                <div class="project-text w-100 my-auto text-center text-lg-left">
                                    <h4 class="text-white">Моторное масло №1</h4>
                                    <p class="mb-0 text-white-50">Описание <br/> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloremque, amet! Esse incidunt perferendis laudantium ipsa optio, excepturi nihil numquam nulla consectetur ullam! Nam ullam laboriosam deserunt iusto consectetur eum maiores?</p>
                                    <hr class="d-none d-lg-block mb-0 ms-0" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Project Two Row-->
                <div class="row gx-0 justify-content-center">
                    <div class="col-lg-6"><img class="img-fluid" src="../../assets/img/2.webp" alt="..." /></div>
                    <div class="col-lg-6 order-lg-first">
                        <div class="bg-black text-center h-100 project">
                            <div class="d-flex h-100">
                                <div class="project-text w-100 my-auto text-center text-lg-right">
                                    <h4 class="text-white">Моторное масло №2</h4>
                                    <p class="mb-0 text-white-50">Описание <br/> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Natus molestias voluptas, enim tempore nisi quidem dolore? Voluptates laboriosam veniam, tempora, beatae vitae ea repudiandae in quae mollitia omnis eius incidunt?</p>
                                    <hr class="d-none d-lg-block mb-0 me-0" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Signup-->
        <section class="signup-section" id="signup">
            <div class="container px-4 px-lg-5">
                <!-- <div class="row gx-4 gx-lg-5">
                    <div class="col-md-10 col-lg-8 mx-auto text-center">
                        <i class="far fa-paper-plane fa-2x mb-2 text-white"></i>
                        <h2 class="text-white mb-5">Subscribe to receive updates!</h2>

                        <form class="form-signup" id="contactForm" data-sb-form-api-token="API_TOKEN">

                            <div class="row input-group-newsletter">
                                <div class="col"><input class="form-control" id="emailAddress" type="email" placeholder="Enter email address..." aria-label="Enter email address..." data-sb-validations="required,email" /></div>
                                <div class="col-auto"><button class="btn btn-primary disabled" id="submitButton" type="submit">Notify Me!</button></div>
                            </div>
                            <div class="invalid-feedback mt-2" data-sb-feedback="emailAddress:required">An email is required.</div>
                            <div class="invalid-feedback mt-2" data-sb-feedback="emailAddress:email">Email is not valid.</div>

                            <div class="d-none" id="submitSuccessMessage">
                                <div class="text-center mb-3 mt-2 text-white">
                                    <div class="fw-bolder">Form submission successful!</div>
                                    To activate this form, sign up at
                                    <br />
                                    <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
                                </div>
                            </div>

                            <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3 mt-2">Error sending message!</div></div>
                        </form>
                    </div>
                </div> -->
            </div>
        </section>
        <!-- Contact-->
        <section class="contact-section bg-black">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5">
                    <div class="col-md-4 mb-3 mb-md-0">
                        <div class="card py-4 h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-map-marked-alt text-primary mb-2"></i>
                                <h4 class="text-uppercase m-0">Наш адрес</h4>
                                <hr class="my-4 mx-auto" />
                                <div class="small text-black-50">Республика Узбекистан, г.Ташкент, Юнусабадский район, массив Киет 56А</div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3 mb-md-0">
                        <div class="card py-4 h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-envelope text-primary mb-2"></i>
                                <h4 class="text-uppercase m-0">E-mail</h4>
                                <hr class="my-4 mx-auto" />
                                <div class="small text-black-50"><a href="#!">info@b-oil.uz</a></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3 mb-md-0">
                        <div class="card py-4 h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-mobile-alt text-primary mb-2"></i>
                                <h4 class="text-uppercase m-0">Телефон</h4>
                                <hr class="my-4 mx-auto" />
                                <div class="small text-black-50">+998 (95) 410-0300</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="social d-flex justify-content-center">
                    <a class="mx-2" href="#!"><i class="fab fa-twitter"></i></a>
                    <a class="mx-2" href="#!"><i class="fab fa-facebook-f"></i></a>
                    <a class="mx-2" href="#!"><i class="fab fa-github"></i></a>
                </div>
            </div>
        </section>
        <!-- Footer-->
        <footer class="footer bg-black small text-center text-white-50"><div class="container px-4 px-lg-5">Copyright &copy; NEXXOL 2022</div></footer>
  </div>
</template>

<script setup>

</script>

<style scoped>

</style>
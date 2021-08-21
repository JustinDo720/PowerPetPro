<template>
  <nav class="navbar is-transparent extended-navbar has-shadow is-dark">
    <!-- Navbar Brand-->
    <div class="navbar-brand">
      <a href="/">
        <img
          src="../assets/ppp_logo2.jpg"
          alt="Power Pet Pro Logo"
          class="is-rounded"
          width="112"
          height="28"
        />
      </a>
    </div>
    <a
      role="button"
      class="navbar-burger"
      aria-label="menu"
      aria-expanded="false"
      data-target="navbarBurger"
      @click="showMobileMenu = !showMobileMenu"
    >
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
    <!-- Start Navbar aka left side -->
    <div class="navbar-start">
      <a class="navbar-item"> Shop </a>
    </div>
    <!-- We are going to use is-active to trigger our burger -->
    <div
      id="navbarBurger"
      class="navbar-menu"
      v-bind:class="{ 'is-active': showMobileMenu }"
    >
      <div class="navbar-item">
        <div class="control has-icons-left has-icons-right">
          <input class="input is-rounded" type="text" placeholder="Search" />
          <span class="icon is-small is-left">
            <i class="fas fa-search"></i>
          </span>
        </div>
      </div>

      <!-- End Navbar aka right side -->
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="dropdown" :class="{ 'is-active': showAccount }">
            <div class="dropdown-trigger">
              <button
                class="button is-medium"
                aria-haspopup="true"
                aria-controls="dropdown-menu3"
                @click="showAccount = !showAccount"
              >
                <span class="icon is-small">
                  <i class="fas fa-user-circle"></i>
                </span>
                <span>Account</span>
                <span class="icon is-small">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu3" role="menu">
              <div class="dropdown-content">
                <a href="#" class="dropdown-item"> Log In </a>
                <a href="#" class="dropdown-item"> Create Account </a>
              </div>
            </div>
          </div>
        </div>
        <div class="navbar-item">
          <button class="button is-medium">
            <i class="fas fa-shopping-bag"></i>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      showMobileMenu: false,
      showAccount: false,
    };
  },
};
</script>

<style scoped>
.extended-navbar {
  font-size: 1.125rem;
  padding: 1rem 4rem;
}
</style>

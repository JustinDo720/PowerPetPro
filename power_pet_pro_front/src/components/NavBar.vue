<template>
  <nav class="navbar is-transparent extended-navbar has-shadow is-dark columns">
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
    <!-- We are going to use is-active to trigger our burger -->
    <div
      id="navbarBurger"
      class="navbar-menu"
      v-bind:class="{ 'is-active': showMobileMenu }"
    >
        <!-- Start Navbar aka left side -->
      <div class="navbar-start">
          <button  class='button navbar-item is-large buttonTransparent' data-show="quickview" data-target="quickviewDefault">
            <span class="icon is-small">
              <i class="fas fa-bars"></i>
            </span>
          </button>
      </div>

      <div id="quickviewDefault" class="quickview">
        <header class="quickview-header">
          <p class="title">Quickview title</p>
          <span class="delete" data-dismiss="quickview"></span>
        </header>
        <div class="quickview-body">
          <div class="quickview-block">
            ...
          </div>
        </div>
        <footer class="quickview-footer">
        </footer>
      </div>

      <div class="navbar-item column is-three-fifths">
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
            <span class="icon is-small">
               <i class="fas fa-shopping-bag"></i>
            </span>
            <span>({{ cartLength }})</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: "NavBar",
  data() {
    return {
      showMobileMenu: false,
      showAccount: false,
    };
  },
  computed:{
    ...mapState(['cart']),
    cartLength(){
      // return this.$store.state.cart.items.length
      let totalLength = 0
      for(let i=0; i < this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }
};
</script>

<style scoped>
.extended-navbar {
  font-size: 1.125rem;
  padding: 1rem 4rem;
}
.buttonTransparent{
  background-color:transparent;
  border: none;
}
</style>

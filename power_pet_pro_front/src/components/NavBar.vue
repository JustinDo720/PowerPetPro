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
        <!-- quick view controller once they press this button it will open up our id=quickviewDeault -->
        <button
          class="button navbar-item is-large buttonTransparent"
          data-show="quickview"
          data-target="quickviewDefault"
        >
          <span class="icon is-small">
            <i class="fas fa-bars"></i>
          </span>
        </button>
      </div>

      <!-- Our quickview menu which will appear to the right once our button is clicked -->
      <div id="quickviewDefault" class="quickview">
        <header class="quickview-header">
          <!-- Using span allows you to be leveled -->
          <span>
            <h3 class="title is-3">
              <strong> Categories </strong>
            </h3>
          </span>
          <span class="delete" data-dismiss="quickview"></span>
        </header>
        <div class="quickview-body">
          <div class="quickview-block">
            <aside class="menu ml-2 mt-2">
              <p class="menu-label">General</p>
              <ul class="menu-list">
                <li v-for="(category, index) in store_categories" :key="index">
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'Category',
                      params: {
                        category_slug: category.get_absolute_url,
                      },
                    }"
                  >
                    {{ category.name }}
                  </router-link>
                </li>
              </ul>
            </aside>
          </div>
        </div>
        <footer class="quickview-footer"></footer>
      </div>

      <div class="navbar-item column is-three-fifths">
        <div class="control has-icons-left has-icons-right">
          <input class="input is-rounded" type="text"
                 placeholder="Search" v-model="searchTerm"
                 @keydown.enter="addSearch"/>
          <span class="icon is-small is-left">
            <i class="fas fa-search"></i>
          </span>
        </div>
      </div>

      <!-- End Navbar aka right side -->
      <div class="navbar-end">
        <div class="navbar-item" v-if="!isAuth">
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
                <router-link :to="{name:'Login'}" >
                  <a class="dropdown-item" @click="showAccount = !showAccount"> Log In </a>
                </router-link>
                <router-link  :to="{name:'Register'}">
                  <a class="dropdown-item" @click="showAccount = !showAccount"> Create Account </a>
                </router-link>

              </div>
            </div>
          </div>
        </div>
        <div class="navbar-item" v-if="isAuth">
          <p>
            Welcome, {{ username }}!
          </p>
        </div>
        <div class="navbar-item">
          <router-link :to="{name:'Cart'}">
              <button class="button is-medium">
              <span class="icon is-small">
                <i class="fas fa-shopping-bag"></i>
              </span>
              <span>({{ cartLength }})</span>
            </button>
          </router-link>

        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "NavBar",
  data() {
    return {
      showMobileMenu: false,
      store_categories: [],
      searchTerm: '',
      showAccount: false
    };
  },
  computed: {
    ...mapState(["cart", "username"]),
    ...mapGetters(['isAuth']),
    cartLength() {
      // return this.$store.state.cart.items.length
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }
      return totalLength;
    },
  },
  methods:{
    async addSearch(){
      await this.$store.commit('addSearch', {searchTerm: this.searchTerm})
      this.$router.push({'name':'Search'})
      this.searchTerm = ''
    },
  },
  created() {
    // we want to grab our categories
    axios.get("/category_list/").then((response) => {
      this.store_categories = response.data; // we are setting our store_categories array to data array
    });
  },
};
</script>

<style scoped>
.extended-navbar {
  font-size: 1.125rem;
  padding: 1rem 4rem;
}
.buttonTransparent {
  background-color: transparent;
  border: none;
}
</style>

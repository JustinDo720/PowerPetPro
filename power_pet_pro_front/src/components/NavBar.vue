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
          <span> Shop </span>
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
            <aside class="menu ml-2 mt-2" v-if="isAdmin">
              <p class="menu-label title is-4">Admin</p>
              <ul class="menu-list">
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'ViewAllMessages',
                    }"
                  >
                    <button class="button is-light is-danger">View All Messages</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'MessageBox',
                    }"
                  >
                    <button class="button is-light is-danger">Add/Edit Message of the Day</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'ViewAllProducts',
                    }"
                  >
                    <button class="button is-light is-danger">View All Products</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'AdminProduct',
                    }"
                  >
                    <button class="button is-light is-danger">Add Product</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'AdminCategory',
                    }"
                  >
                    <button class="button is-light is-danger">Add Category</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'MissionStatementBox',
                    }"
                  >
                    <button class="button is-light is-danger">Add Mission Statement</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'MissionStatementTopicBox',
                    }"
                  >
                    <button class="button is-light is-danger">Add Mission Statement Topic</button>
                  </router-link>
                </li>
                <li>
                  <router-link
                    data-dismiss="quickview"
                    :to="{
                      name: 'MissionDetailsBox',
                    }"
                  >
                    <button class="button is-light is-danger">Add Mission Details</button>
                  </router-link>
                </li>
                <li>
                    <router-link
                      :to="{
                        name: 'QuestionControl',
                      }"
                    >
                      <button class="button is-light is-danger">Add/View Questions</button>
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{
                        name: 'AllFeedbacks',
                      }"
                    >
                      <button class="button is-light is-danger">View All User Feedback</button>
                    </router-link>
                  </li>

              </ul>
            </aside>

            <aside class="menu ml-2 mt-2">
              <p class="menu-label title is-4">General</p>
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
                    <button class="button is-light is-link">{{ category.name }}</button>
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
          <input
            class="input is-rounded"
            type="text"
            placeholder="Search"
            v-model="searchTerm"
            @keydown.enter="addSearch"
          />
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
                <router-link :to="{ name: 'Login' }">
                  <a class="dropdown-item" @click="showAccount = !showAccount">
                    Log In
                  </a>
                </router-link>
                <router-link :to="{ name: 'Register' }">
                  <a class="dropdown-item" @click="showAccount = !showAccount">
                    Create Account
                  </a>
                </router-link>
                <router-link :to="{ name: 'Reactivate' }">
                  <a class="dropdown-item" @click="showAccount = !showAccount">
                    Resend Activation Email
                  </a>
                </router-link>
                <router-link :to="{ name: 'ResetPassword' }">
                  <a class="dropdown-item" @click="showAccount = !showAccount">
                    Reset Password
                  </a>
                </router-link>
                <router-link :to="{ name: 'CheckOrder' }">
                  <a class="dropdown-item" @click="showAccount = !showAccount">
                    Check Order
                  </a>
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="navbar-item" v-if="isAuth">
          <span class="mr-1">
            <p
              class="subtitle is-5"
              :class="{ 'has-text-white-bis': !showMobileMenu }"
              v-if="isAdmin"
            >
              Welcome Admin,
              <router-link :to="{ name: 'Profile' }"
                >{{ username }}!&nbsp;</router-link
              >
            </p>
            <p
              class="subtitle is-5"
              :class="{ 'has-text-white-bis': !showMobileMenu }"
              v-else
            >
              Welcome,
              <router-link :to="{ name: 'Profile' }"
                >{{ username }}!&nbsp;</router-link
              >
            </p>
          </span>
          <span>
              <button class="button is-small" @click="logOut()">
                <span> Log Out </span>
                <span class="icon is-medium">
                  <i class="fas fa-sign-out-alt"></i>
                </span>
              </button>
            </span>
          <div class="navbar-item">
            <div class="dropdown" :class="{'is-active' : showFunction}">
              <div class="dropdown-trigger">
                <button
                    class="button is-small"
                    aria-haspopup="true"
                    aria-controls="dropdown-menu4"
                    @click="showFunction = !showFunction"
                >
                  <span class="icon is-small">
                    <i class="fas fa-angle-down"></i>
                  </span>
                </button>
              </div>
              <div class="dropdown-menu" id="dropdown-menu4" role="menu">
                <div class="dropdown-content">
                  <router-link :to="{ name: 'CheckOrder' }">
                    <a class="dropdown-item" @click="showFunction = !showFunction">
                      Check Your Order
                    </a>
                  </router-link>

                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="navbar-item">
          <router-link :to="{ name: 'Cart' }">
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
import Cookies from "cookies-js";

export default {
  name: "NavBar",
  data() {
    return {
      showMobileMenu: false,
      searchTerm: "",
      showAccount: false,
      isAdmin: false,
      showFunction: false,
    };
  },
  computed: {
    ...mapState(["cart", "username", "store_categories"]),
    ...mapGetters(["isAuth"]),
    cartLength() {
      // return this.$store.state.cart.items.length
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += parseInt(this.cart.items[i].quantity);
      }
      return totalLength;
    },
  },
  methods: {
    async addSearch() {
      await this.$store.commit("addSearch", { searchTerm: this.searchTerm });
      this.$router.push({ name: "Search" });
      this.searchTerm = "";
    },
    logOut() {
      this.$store.commit("logoutUser");
      this.$router.push({ name: "Home" });
    },
  },
  created() {
    // we want to grab our categories
    axios.get("/category_list/").then((response) => {
      this.$store.commit("update_categories", { categories: response.data });
    });
     /*
    * The main Problem is that is_staff is actually string of 'true' and we can't use our store because vue life cycle
    * comes first before our store initialize so we need to make sure we use Cookies to grab our data. Therefore,
    * we need to change is_staff from string 'true'/'false' to it's boolean value. Otherwise v-if will not work as
    * intended because they'll read 'false' as true as its not blank. So let's use JSON.parse.
    *
    * JSON.parse will parse our string value which converts the type of variable into boolean
    * */
    if(Cookies('is_staff')){
      this.isAdmin = JSON.parse(Cookies('is_staff'))
    }
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

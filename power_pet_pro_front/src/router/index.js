import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Product from "../views/Product.vue";
import Category from "../views/Category";
import Search from "../views/Search";
import Cart from "../views/Cart";
import LogIn from "../views/LogIn";
import Register from "../views/Register";
import Profile from "../views/Profile";
import Activate from "../views/Activate";
import ResetPassword from "../views/ResetPassword";
import ResetPasswordConfirmation from "../views/ResetPasswordConfirmation";
import store from "../store"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue"),
  // },
  {
    path: "/product_list/product_detail/:category_slug/:product_slug/", // we have : to catch these values
    name: "Product",
    component: Product,
  },
  {
    path: "/category_list/category_detail/:category_slug/",
    name: "Category",
    component: Category,
  },
  {
    path: "/product_list/search",
    name: "Search",
    component: Search
  },
  {
    path: '/cart/',
    name: "Cart",
    component: Cart,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login/',
    name: "Login",
    component: LogIn,
  },
  {
    path: '/register/',
    name: "Register",
    component: Register,
  },
  {
    path: '/profile/',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/activate/:uid/:token',
    name: 'Activate',
    component: Activate,
  },
  {
    path: '/reset_password/',
    name: 'ResetPassword',
    component: ResetPassword, // This will grab the email and send an email with the reset link
  },
  {
    path: '/password/reset/confirm/:uid/:token',
    name: 'ResetPasswordConfirmation',
    component: ResetPasswordConfirmation // This will actually reset the password
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

store.dispatch('initializeStore').then(()=> {
  router.beforeEach((to, from, next) => {
    if (to.matched.some(response => response.meta.requiresLogin)) {
      if (!store.getters.isAuth) {
        next({name: 'Login'})
      } else {
        next()
      }
    } else {
      next()
    }
  })
})
export default router;

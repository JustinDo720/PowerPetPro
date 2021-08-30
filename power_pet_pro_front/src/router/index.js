import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Product from "../views/Product.vue";
import Category from "../views/Category";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

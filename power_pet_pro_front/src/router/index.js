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
import Reactivate from "../views/Reactivate";
import MessageBox from "../views/MessageBox";
import AdminProduct from "../views/AdminProduct";
import AdminCategory from "../views/AdminCategory";
import ViewAllMessages from "../views/ViewAllMessages";
import ViewAllProducts from "../views/ViewAllProducts";
import MissionStatementBox from "../views/MissionStatementBox";
import MissionStatementTopicBox from "../views/MissionStatementTopicBox";
import Topic from "../views/Topic";
import MissionDetailsBox from "../views/MissionDetailsBox";
import Checkout from "../views/Checkout";
import Success from "../views/Success";
import Orders from "../views/Orders";
import IndividualOrder from "../views/IndividualOrder";
import SubmitFeedback from "../views/SubmitFeedback";
import QuestionControl from "../views/QuestionControl";
import AllFeedbacks from "../views/AllFeedbacks";
import CheckOrder from "../views/CheckOrder";
import store from "../store";

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
    path: "/product_list/search/",
    name: "Search",
    component: Search,
  },
  {
    path: "/cart/",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/login/",
    name: "Login",
    component: LogIn,
  },
  {
    path: "/register/",
    name: "Register",
    component: Register,
  },
  {
    path: "/profile/",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/activate/:uid/:token",
    name: "Activate",
    component: Activate,
  },
  {
    path: "/reset_password/",
    name: "ResetPassword",
    component: ResetPassword, // This will grab the email and send an email with the reset link
  },
  {
    path: "/password/reset/confirm/:uid/:token",
    name: "ResetPasswordConfirmation",
    component: ResetPasswordConfirmation, // This will actually reset the password
  },
  {
    path: "/reactivate/",
    name: "Reactivate",
    component: Reactivate,
  },
  {
    path: "/admin/messagebox/",
    name: "MessageBox",
    component: MessageBox,
  },
  {
    path: "/admin/admin_product/",
    name: "AdminProduct",
    component: AdminProduct,
  },
  {
    path: "/admin/admin_category/",
    name: "AdminCategory",
    component: AdminCategory,
  },
  {
    path: "/admin/view_all_messages/",
    name: "ViewAllMessages",
    component: ViewAllMessages,
  },
  {
    path: "/admin/view_all_products/",
    name: "ViewAllProducts",
    component: ViewAllProducts,
  },
  {
    path: "/admin/mission_statement_box/",
    name: "MissionStatementBox",
    component: MissionStatementBox,
  },
  {
    path: "/admin/mission_statement_topic_box/",
    name: "MissionStatementTopicBox",
    component: MissionStatementTopicBox,
  },
  {
    path: "/mission_statement/topic/:topic_slug/",
    name: "Topic",
    component: Topic,
  },
  {
    path: "/mission_statement/topic/add_details/",
    name: "MissionDetailsBox",
    component: MissionDetailsBox,
  },
  {
    path: "/cart/checkout/",
    name: "Checkout",
    component: Checkout,
  },
  {
    path: "/cart/checkout/:user_id/order/:order_id/success/",
    name: "Success",
    component: Success,
  },
  {
    path: "/profile/:id/orders/",
    name: "Orders",
    component: Orders,
  },
  {
    path: "/profile/:id/order/:order_number/",
    name: "IndividualOrder",
    component: IndividualOrder,
  },
  {
    path: '/submit_feedback/',
    name: "SubmitFeedback",
    component: SubmitFeedback,
  },
  {
    path: '/admin/question_control/',
    name: "QuestionControl",
    component: QuestionControl,
  },
  {
    path: '/admin/all_feedbacks/',
    name: "AllFeedbacks",
    component: AllFeedbacks,
  },
  {
    path: '/check_order/',
    name: "CheckOrder",
    component: CheckOrder,
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

store.dispatch("initializeStore").then(() => {
  router.beforeEach((to, from, next) => {
    if (to.matched.some((response) => response.meta.requiresLogin)) {
      if (!store.state.accessToken) {
        next({ name: "Login" });
      } else {
        next();
      }
    } else {
      next();
    }
  });
});
export default router;

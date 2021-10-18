import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "../node_modules/bulma/css/bulma.css";
import axios from "axios";
import Cookies from "cookies-js";

// we could set a default for axios so now we don't have to keep putting this before our paths
axios.defaults.baseURL = "http://localhost:8000/";

Cookies.defaults = {
  path: "/",
  secure: true,
};

createApp(App).use(store).use(router).mount("#app");

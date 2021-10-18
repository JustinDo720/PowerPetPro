import { createStore } from "vuex";
import axios from "axios";
import Cookies from "cookies-js";

// We will use this function to save our tokens
function saveTokens(username, user_id, accessToken, refreshToken) {
  Cookies.set("username", username, { expires: 604800 });
  Cookies.set("user_id", user_id, { expires: 604800 });
  Cookies.set("accessToken", accessToken, { expires: 604800 });
  Cookies.set("refreshToken", refreshToken, { expires: 604800 });
}

export default createStore({
  state: {
    latestProducts: "", // we are going to use this state to store our 5 products in case we need to use it elsewhere
    cart: {
      items: [],
    },
    isAuthenticated: false,
    username: "",
    user_id: null,
    accessToken: "",
    refreshToken: "",
    isLoading: false, // We are going to add a loading bar for things that are loading
    searchTerm: "",
  },
  mutations: {
    // mutations have state as their parameters as they're the only ones that could actually change state
    grabLatestProducts(state, latestProductsProxy) {
      // We do get the proxy but we want to make sure we throw in an object to our latestProducts state
      state.latestProducts = latestProductsProxy.latestProductsProxy;
    },
    // Let's go ahead and make a function that changes the cart items
    addToCart(state, { item_object }) {
      let item = item_object; // this will allow us to just access products or quantity must easier
      // We want to check if the product exist using the ids.
      // So instead of using cart_item.product.id like before we are just using .product because .product is the id
      const exists = state.cart.items.filter(
        (cart_item) => cart_item.product === item.product.id
      );
      // if our exists has a length > 0 that means the product exist and we need to handle that
      if (exists.length) {
        // each time the product exists we are incrementing our quantity for a specific product instead of adding same
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity); // exists[0].quantity = total quant
        if (state.accessToken) {
          let headers = { Authorization: `Bearer ${state.accessToken}` };
          axios.put(
            `profile_list/user_profile/${state.user_id}/cart/${item.product.id}/`,
            {
              profile: state.user_id,
              product: item.product.id,
              quantity: exists[0].quantity, // if we are doing a put request we just need to change the quantity
            },
            { headers }
          );
        }
      } else {
        // this is a new product so we want to just push this to our cart
        if (state.accessToken) {
          let headers = { Authorization: `Bearer ${state.accessToken}` };
          axios
            .post(
              `profile_list/user_profile/${state.user_id}/cart/${item.product.id}/`,
              {
                profile: state.user_id,
                product: item.product.id,
                quantity: item.quantity,
              },
              { headers }
            )
            .then((r) => {
              console.log(r);
            });
        }
        // before we push our item we want it to be in our specific format
        // since our products are no longer under product key we need the name, price and abs_url
        // the main reason why we need this format is because of our serializer returning this specific format
        // rather than have all product details under the key product, we have the necessary product info here
        let cart_item_format = {
          profile: state.user_id,
          product: item.product.id,
          quantity: item.quantity,
          name: item.product.name,
          price: item.product.price,
          get_absolute_url: item.product.get_absolute_url,
        };
        // once we make this new format, we are going to push it
        state.cart.items.push(cart_item_format);
      }

      // regardless of exists, we need to update our localstorage cart with state card for initializeStore
      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    // Now we could use setIsLoading for where we want to load usually before our api request because it takes some time
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    addSearch(state, searchTerm) {
      state.searchTerm = searchTerm.searchTerm;
    },
    loginUser(state, { username, accessToken, refreshToken, user_id }) {
      state.username = username;
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
      state.user_id = user_id;

      // We don't need to save these tokens because we are already running an initializeStore right after this
      // saveTokens(state.username, state.user_id, state.accessToken, state.refreshToken)
    },
    logoutUser(state) {
      // we need to destroy auth details
      state.username = "";
      state.accessToken = "";
      state.refreshToken = "";
      state.user_id = "";

      Cookies.expire("username");
      Cookies.expire("accessToken");
      Cookies.expire("refreshToken");
      Cookies.expire("user_id");

      // we also need to take care of cart
      state.cart.items = "";
      localStorage.removeItem("cart");
    },
    initializeStore(state, { username, user_id, accessToken, refreshToken }) {
      if (localStorage.getItem("cart")) {
        // If cart exist then we will set our state to the cart
        // We use JSON.parse to grab an object wrapped in strings because of Local Storage
        let headers = { Authorization: `Bearer ${accessToken}` };
        axios
          .get(`profile_list/user_profile/${user_id}/cart/`, { headers })
          .then((response) => {
            for (let key in response.data) {
              state.cart.items.push(response.data[key]);
            }
          });
        // After you set cart items in state we also need to set that in Cart so
        localStorage.setItem("cart", JSON.stringify(state.cart));
      } else {
        // NOTE: Localstorage usually takes strings thats why we need stringify to wrap our obj in string format
        // we dont have cart in our localstorage so lets set it
        console.log("Why is is that when we refresh cart this comes back?");
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }

      state.username = username;
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
      state.user_id = user_id;
      saveTokens(
        state.username,
        state.user_id,
        state.accessToken,
        state.refreshToken
      );
    },
  },
  actions: {
    initializeStore(context) {
      if (
        Cookies("username") &&
        Cookies("user_id") &&
        Cookies("accessToken") &&
        Cookies("refreshToken")
      ) {
        const username = Cookies("username");
        const user_id = Cookies("user_id");
        const accessToken = Cookies("accessToken");
        const refreshToken = Cookies("refreshToken");

        axios
          .post("http://localhost:8000/auth/jwt/verify/", {
            token: accessToken,
          })
          .then(() => {
            context.commit("initializeStore", {
              username: username,
              user_id: user_id,
              accessToken: accessToken,
              refreshToken: refreshToken,
            });
          })
          .catch((err) => {
            console.log(err.response.data);
            axios
              .post("/api/token/refresh/", {
                refresh: refreshToken,
              })
              .then((response) => {
                console.log(response.data);
                context.commit("initializeStore", {
                  username: username,
                  user_id: user_id,
                  accessToken: response.data.access,
                  refreshToken: response.data.refresh, // this is possible because of rotating refresh in settings
                });
              });
          });
      }
    },
    // we are going to need an action for loginUser because we will be committing two mutations
    loginUser(context, { username, accessToken, refreshToken, user_id }) {
      // once we commit loginUser which will save the tokens and update our state
      context.commit("loginUser", {
        username: username,
        accessToken: accessToken,
        refreshToken: refreshToken,
        user_id: user_id,
      });
      // we need to commit a initialize store so we don't have to force refresh a page
      // this will allow us to run our get request
      context.commit("initializeStore", {
        username: username,
        user_id: user_id,
        accessToken: accessToken,
        refreshToken: refreshToken,
      });
    },
  },
  modules: {},
  getters: {
    isAuth(state) {
      return state.accessToken !== "";
    },
  },
});

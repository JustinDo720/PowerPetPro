<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-2">Cart</h1>
      </div>
      <div class="column is-12 box">
        <table
          class="table is-striped is-fullwidth"
          v-if="cart.items.length > 0"
        >
          <!-- thead is the top part of our table-->
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <!-- We will have an empty column for our controls like delete -->
              <th></th>
            </tr>
          </thead>
          <!--- The middle section of our table -->
          <tbody>
            <CartBox
              v-for="(cart_item, index) in cart.items"
              :key="index"
              :cart_item="cart_item"
            ></CartBox>
          </tbody>
        </table>
        <p v-else>You currently have no items in your cart.</p>
        <!-- We are going to need the total amount and proceed to checkout -->
        <div class="column is-12">
          <h2 class="subtitle">Summary</h2>
          <p>
            <strong>${{ cartTotalPrice.toFixed(2) }}</strong
            >, {{ cartTotalLength }} items
          </p>
          <button class="button is-medium mt-4 is-info is-outlined" v-if="cart.items.length > 0">
            <router-link :to="{ name: 'Checkout' }">
              &raquo; Proceed to checkout
            </router-link>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CartBox from "../components/CartBox";

import { mapState } from "vuex";

export default {
  name: "Cart",
  computed: {
    ...mapState(["cart"]),
    cartTotalPrice() {
      let totalPrice = 0;
      for (
        let item_index = 0;
        item_index < this.cart.items.length;
        item_index++
      ) {
        // We need to make sure we take quantity into account
        if (this.cart.items[item_index].quantity >= 2) {
          totalPrice +=
            this.cart.items[item_index].quantity *
            this.cart.items[item_index].price;
        } else {
          // Since we are doing calculations we need the number form. Price is in string format
          totalPrice += Number(this.cart.items[item_index].price);
        }
      }
      // Once we finish to need to make sure we update our localstorage
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
      return totalPrice;
    },
    cartTotalLength() {
      let totalLength = 0;
      for (
        let item_quantity = 0;
        item_quantity < this.cart.items.length;
        item_quantity++
      ) {
        totalLength += this.cart.items[item_quantity].quantity;
      }
      return totalLength;
    },
  },
  components: {
    CartBox,
  },
};
</script>

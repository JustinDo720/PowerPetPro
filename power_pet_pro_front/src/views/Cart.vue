<template>
  <div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-2">
            Cart
        </h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-striped is-fullwidth" v-if="cart.items.length > 0">
          <!-- thead is the top part of our table-->
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <!--- The middle section of our table -->
          <tbody>
            <CartBox v-for="(cart_item, index) in cart.items"
                     :key="index"
                     :cart_item="cart_item"></CartBox>
          </tbody>

        </table>
        <p v-else>
          You currently have no items in your cart.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import CartBox from "../components/CartBox";

import { mapState } from 'vuex'

export default{
  name: 'Cart',
  computed:{
    ...mapState(['cart'])
  },
  components:{
    CartBox
  }
}
</script>
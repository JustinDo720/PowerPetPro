<template>
  <tr>
    <td>
      <router-link :to="productUrl">
        {{ cart_item.product.name }}
      </router-link>
    </td>
    <td>
      ${{ cart_item.product.price }}
    </td>
    <td>

      <div class="buttons has-addons are-small">
        x{{ cart_item.quantity }}&nbsp;
        <button class="button is-success is-inverted" @click="increaseQuantity(cart_item)">
          <i class="fas fa-plus"></i>
        </button>
        <button class="button is-danger is-inverted" @click="decreaseQuantity(cart_item)">
          <i class="fas fa-minus"></i>
        </button>

      </div>
    </td>
    <td>
      ${{ totalPrice.toFixed(2) }}
    </td>
    <td>
       <button class="delete" @click="removeItem(cart_item)"><i class="fas fa-times"></i></button>
    </td>
  </tr>
</template>
<script>
import { mapState } from 'vuex'

export default{
  name: 'CartBox',
  props:{
    cart_item: Object
  },
  computed:{
    ...mapState(['cart']),
    totalPrice(){
      let total = this.cart_item.product.price * this.cart_item.quantity
      return total
    },
    productUrl(){
      let url = `/product_list/product_detail${this.cart_item.product.get_absolute_url}`
      return url
    }
  },
  methods:{
    decreaseQuantity(cart_item){
      // apparently by changing the quantity it also changes the cart items which is weird???
      cart_item.quantity -= 1
      this.updateCart()
    },
    increaseQuantity(cart_item){
      // you don't need to change the state because if its an object in an array on an obj it automatically changes
      // I thought you needed to commit a mutation to update the cart_item.quantity but this automatically changes it
      cart_item.quantity += 1
      this.updateCart()
    },
    updateCart(){
      // by updating the cart our initalizeStorage will make sure the cart is up to date
      // since increasing the quantity already changes the state all we need to do is update our storage for refresh
      localStorage.setItem('cart', JSON.stringify(this.cart))
    },
    removeItem(cart_item){
      // we need to find the item's index, use splice to get rid of the item from cart and then update our cart
      let cart_item_index = this.cart.items.findIndex((element) => element.product.id === cart_item.product.id)
      // splice(index_to_remove, delete_count)
      this.cart.items.splice(cart_item_index, 1)
      this.updateCart()
    }
  }
}
</script>
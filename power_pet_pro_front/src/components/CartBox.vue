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
  </tr>
</template>
<script>

export default{
  name: 'CartBox',
  props:{
    cart_item: Object
  },
  computed:{
    totalPrice(){
      let total = this.cart_item.product.price * this.cart_item.quantity
      console.log(total)
      return total
    },
    productUrl(){
      let url = `/product_list/product_detail${this.cart_item.product.get_absolute_url}`
      console.log(url)
      return url
    }
  },
  methods:{
    decreaseQuantity(cart_item){
      cart_item.quantity -= 1
      this.updateCart()
    },
    increaseQuantity(cart_item){
      cart_item.quantity += 1
      this.updateCart()
    },
    updateCart(){
      // by updating the cart our initalizeStorage will make sure the cart is up to date
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    }
  }
}
</script>
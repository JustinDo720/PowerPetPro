<template>
  <div>
    <div v-for="(cart_item, index) in cart.items" :key="index">
        {{ cart_item }}
      <hr>
    </div>

  </div>
</template>
<script>
import { mapState } from 'vuex'

export default{
  name: 'Cart',
  computed:{
    ...mapState(['cart'])
  },
}
</script>
<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        Order #{{ order.id }}
      </p>
       <p class="card-header-title">
        Total ${{ order.paid_amount }}
      </p>
    </header>
    <div class="columns">
      <div class="column">
       <div v-for="(order_item, key) in order.items.slice(0,2)" :key="key">
          <div class="card-content" v-if="order_item.photo">
            <div class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img :src="order_item.photo" alt="product-image">
                </figure>
              </div>
              <div class="media-content">
                <router-link :to="`/product_list/product_detail${order_item.get_absolute_url}`">
                  <p class="title is-5 has-text-link">
                    {{ order_item.name }}
                  </p>
                </router-link>
                <p class="subtitle is-6"> ${{ order_item.price }} x{{ order_item.quantity }}</p>
              </div>
            </div>
          </div>
          <div class="card-content" v-else>
            <div class="content">
              <div class="content">
                <router-link :to="`/product_list/product_detail${order_item.get_absolute_url}`">
                  <h5 class="has-text-link">
                    {{ order_item.name }}
                  </h5>
                </router-link>
                <p>
                  ${{ order_item.price }}
                  x{{ order_item.quantity }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="card-content">
            <div class="content">
              <div class="box">
                <strong>Delivered To: </strong> {{ order.first_name }} {{ order.last_name }} <br>
                <strong>Order Date: </strong>  {{ dateParse(order.created_at) }} <br>
                <strong>Delivery Address: </strong> {{ order.address }}, {{ order.city }}, {{ order.state }}
              </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

export default{
  name: "OrderBox",
  props:{
    order: Object
  },
  methods: {
     dateParse( date ){
       let new_date = new Date(date.slice(0,4),date.slice(5,7) - 1,date.slice(8,10))
       var options = { month: 'long'};
       let month = new Intl.DateTimeFormat('en-US', options).format(new_date)
       return `${month} ${new_date.getDate()} ${new_date.getFullYear()}`
     }
  },

}
</script>
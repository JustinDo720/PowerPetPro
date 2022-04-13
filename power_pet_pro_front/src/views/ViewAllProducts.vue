<template>
  <table class="table is-striped is-fullwidth is-hoverable">
    <thead>
      <tr>
        <th>Product Name</th>
        <th>Category Name</th>
        <th>Price</th>
        <th>Limited Description</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(product, index) in products" :key="index">
        <th>
          <router-link :to="productUrl(product.get_absolute_url)">
            {{ product.name }}
          </router-link>
        </th>
        <th>{{ product.category_name }}</th>
        <th>{{ product.price }}</th>
        <th>{{ product.limited_description }}</th>
        <th>
          <button
            class="button is-warning is-ghost"
            @click="edit_mode_activated(product)"
          >
            <i class="fas fa-pencil-alt"></i></button
          >&nbsp;
          <button
            class="button is-danger is-ghost"
            @click="delete_mode_activated(product)"
          >
            <i class="fas fa-trash"></i>
          </button>
        </th>
      </tr>
    </tbody>
  </table>
  <nav class="pagination is-centered" role="navigation" aria-label="pagination">
    <button class="pagination-previous" v-if="previous" @click="changeView(previous)">
      Previous
    </button>
    <button class="pagination-next" v-if="next" @click="changeView(next)">Next page</button>
    <ul class="pagination-list">
      <li>
        <div class="box">Total Items: {{ totalProductCount }}</div>
      </li>
      <li>
        <div class="box">Current Page: {{ currPage }}</div>
      </li>
    </ul>
  </nav>

  <!-- Edit Modal -->
  <div class="modal" :class="{ 'is-active': edit_mode }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Edit Product</p>
        <button
          class="delete"
          aria-label="close"
          @click="toggle_mode('e')"
        ></button>
      </header>
      <section class="modal-card-body">
        <!-- Content ... -->

       <div class="field">
         <strong>Product Name: </strong>
         <input class="input is-warning" type="text" v-model="chosen_product_name">
       </div>
        <div class="field">
         <strong>Product Category: </strong><br>
         <div class="select is-warning">
          <select v-model="chosen_product_category">
            <option v-for="(category, index) in categories" :key="index">
              {{ category.name }}
            </option>
          </select>
        </div>
       </div>
       <div class="field">
         <strong>Product Description: </strong>
         <textarea class="textarea is-warning" v-model="chosen_product_description"></textarea>
       </div>
       <div class="field">
         <strong>Product Price: </strong>
         <input class="input is-warning" type="number" v-model="chosen_product_price">
       </div>
        <div id="file-js-example" class="file has-name is-centered">
                <label class="file-label">
                  <input
                    class="file-input is-warning"
                    type="file"
                    name="resume"
                    v-bind="chosen_product_picture"
                    @change="onFileSelected"
                  />
                  <span class="file-cta">
                    <span class="file-icon">
                      <i class="fas fa-upload"></i>
                    </span>
                    <span class="file-label"> Choose a file… </span>
                  </span>
                  <span class="file-name"> {{ default_image_name }} </span
                  >&nbsp;
                  <span>
                    <button
                      class="button is-danger is-outlined"
                      @click.prevent="remove_file()"
                    >
                      <span>Remove File </span>
                      <span class="icon is-small">
                        <i class="fas fa-times"></i>
                      </span>
                    </button>
                  </span>
                </label>
              </div>

      </section>
      <footer class="modal-card-foot">
         <button class="button is-success" @click="edit_product()">Save changes</button>
        <button class="button" @click="toggle_mode('e')">Cancel</button>
      </footer>
    </div>
  </div>

  <!-- Delete Modal -->
  <div class="modal" :class="{ 'is-active': delete_mode }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm Delete Product</p>
        <button
          class="delete"
          aria-label="close"
          @click="toggle_mode('d')"
        ></button>
      </header>
      <div class="modal-card-body">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3" v-if="default_image_name">
              <img :src="chosen_product.image" alt="Product-Image" />
            </figure>
          </div>
          <div class="card-content has-text-centered">
            <p class="title is-4">
              {{ chosen_product_name }}
            </p>
            <p class="subtitle is-6">${{ chosen_product_price }}</p>
          </div>

          <div class="content">
            <div class="box">
              {{ chosen_product_description }}
            </div>
          </div>
        </div>
      </div>
      <footer class="modal-card-foot">
        <button class="button is-danger" @click="delete_product()">
          Delete Product
        </button>
        <button class="button" @click="toggle_mode('d')">
          Cancel
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js";
import { mapState } from "vuex";
import { toast } from "bulma-toast";

export default {
  name: "ViewAllProducts",
  data() {
    return {
      products: [],
      categories: [],
      next: "",
      previous: "",
      totalProductCount: null,
      currPage: null,
      edit_mode: false,
      delete_mode: false,
      default_image_name: "No Files Selected",
      // Product chosen by admin
      chosen_product_id: '',
      chosen_product_picture: '',
      chosen_product_name: '',
      chosen_product_description: '',
      chosen_product_price: '',
      chosen_product_productUrl: '',
      chosen_product_category: '',
      // this could be an easy fix to all your problems if you just set the product to chosen_product
      chosen_product: '',   // access the price and stuff just from chosen_product.........................
    };
  },
  computed: {
    ...mapState(["accessToken"]),
  },
  methods: {
    onFileSelected(event) {
      this.chosen_product_picture = event.target.files[0];
      console.log(this.chosen_product_picture);
      this.default_image_name = this.chosen_product_picture.name;
    },
    remove_file(){
      this.default_image_name = "No Files Selected";
      this.chosen_product_picture = '';
    },
    productUrl(abs_url) {
      return `/product_list/product_detail${abs_url}`;
    },
    changeView(url) {
      if (url !== null) {
        axios
          .get(url, {
            headers: { Authorization: `Bearer ${Cookies("accessToken")}` },
          })
          .then((response) => {
            this.products = response.data.results;
            if(response.data.next){
              this.next = response.data.next;
            }else{
              this.next = ''
            }
            if(response.data.previous){
              this.previous = response.data.previous;
            }else{
              this.previous = ''
            }
            this.totalProductCount = response.data.count;

            if(response.data.next){
              this.currPage = parseInt(response.data.next.slice(-1)) - 1;
            } else {
              this.currPage = parseInt(response.data.previous.slice(-1)) + 1;
            }

          });
      }
    },
    toggle_mode(mode){
      if(mode === 'e'){
        this.edit_mode = !this.edit_mode
      } else if(mode === 'd'){
        this.delete_mode = !this.delete_mode
      }

      this.default_image_name = ''
      this.chosen_product_picture = ''
    },
    edit_mode_activated(product) {
      this.edit_mode = !this.edit_mode;
      this.chosen_product_id = product.id;
      if(product.get_image_name){
        this.default_image_name = product.get_image_name;
      }
      this.chosen_product_name = product.name;
      this.chosen_product_description = product.description;
      this.chosen_product_price = product.price;
      this.chosen_product_productUrl = product.get_absolute_url
      this.chosen_product_category = product.category_name
      this.chosen_product_productUrl = this.productUrl(
        product.get_absolute_url
      );
    },
    delete_mode_activated(product) {
      this.delete_mode = !this.delete_mode;
      this.chosen_product_id = product.id;
      this.chosen_product_category = product.category_name
      if(product.get_image_name){
        this.default_image_name = product.get_image_name;
        this.chosen_product = product
      }
      this.chosen_product_name = product.name;
      this.chosen_product_description = product.description;
      this.chosen_product_price = product.price;
      this.chosen_product_productUrl = this.productUrl(
        product.get_absolute_url
      );

    },
    delete_product() {
      axios
        .delete(`admin_panel/product_list/update/${this.chosen_product_id}/`, {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        .then((response) => {
          toast({
            message: response.data.success,
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          });
          this.delete_mode = !this.delete_mode;
        });
    },
    edit_product(){
      // When uploading images we are going to use FormData Axios rather than our original way
      const fd = new FormData();
      let category_id = this.categories.find((category)=> category.name === this.chosen_product_category).id
      fd.append("category", category_id);
      fd.append("name", this.chosen_product_name);
      fd.append("price", parseInt(this.chosen_product_price));
      fd.append("description", this.chosen_product_description);
      fd.append("image", this.chosen_product_picture);
       axios({
          url: `admin_panel/product_list/update/${this.chosen_product_id}/`,
          method: "PUT",
          data: fd,
          headers: { Authorization: `Bearer ${this.accessToken}` },
        }).then(()=>{
          toast({
            message: `${this.chosen_product_name} has been successfully updated`,
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          })
          this.edit_mode = !this.edit_mode
       })
    }
  },
  created() {
    axios
      .get("product_list/", {
        headers: { Authorization: `Bearer ${Cookies("accessToken")}` },
      })
      .then((response) => {
        this.products = response.data.results;
        if(response.data.next){
          this.next = response.data.next;
        }else{
          this.next = ''
        }
        if(response.data.previous){
          this.previous = response.data.previous;
        }else{
          this.previous = ''
        }
        this.totalProductCount = response.data.count;
        this.currPage = parseInt(response.data.next.slice(-1)) - 1;
        axios.get('category_list/').then((response)=>{

          this.categories = response.data
        })
      });
  },
};
</script>

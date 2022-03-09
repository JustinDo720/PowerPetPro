<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Product</p>
        <hr />
        <p class="subtitle">
          Please Enter the follow information below to add a product
        </p>

        <div class="columns is-centered">
          <div class="column is-5" v-if="show_added_product">
            <div class="box">
              <div class="card">
                <div class="card-image" v-if="saved_photo_url">
                  <figure class="image is-4by3">
                    <img :src="saved_photo_url" :alt="saved_photo_url" />
                  </figure>
                </div>
                <div class="card-content">
                  <div class="content">
                    <div class="is-centered">
                      <h1 class="title is-2">
                        {{ product_name }}
                      </h1>
                    </div>
                    <div>
                      <h2 class="subtitle is-3">
                        Category: {{ chosen_category }}
                      </h2>
                    </div>
                    <div>
                      <h2 class="subtitle is-3">Price: ${{ product_price }}</h2>
                    </div>
                    <hr />
                    <div>
                      <h2 class="subtitle is-4">
                        Description: {{ product_description }}
                      </h2>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_product()">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>
              <div class="field">
                <h1 class="title is-4">Category:</h1>
                <div class="select is-medium is-rounded">
                  <select v-model="chosen_category">
                    <option
                      v-for="(category, index) in store_categories"
                      :key="index"
                    >
                      {{ category.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="field">
                <input
                  class="input is-medium"
                  type="text"
                  placeholder="Product Name"
                  v-model="product_name"
                />
              </div>
              <div class="field">
                <div class="control">
                  <textarea
                    class="textarea"
                    placeholder="Description"
                    v-model="product_description"
                  ></textarea>
                </div>
              </div>

              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-tags"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="number"
                    placeholder="Product Price"
                    v-model="product_price"
                  />
                </div>
              </div>
              <div id="file-js-example" class="file has-name is-centered">
                <label class="file-label">
                  <input
                    class="file-input"
                    type="file"
                    name="resume"
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
              <br />
              <button class="button is-success">Submit Product</button>
              <div>
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
import { mapState } from "vuex";
import { toast } from "bulma-toast";

export default {
  name: "AdminProduct",
  data() {
    return {
      chosen_category: "",
      product_name: "",
      product_description: "",
      product_image: null,
      default_image_name: "No Files Selected",
      product_price: 0,
      error_message: "",
      // These data are only configured after the admin posts valid data
      show_added_product: false,
      saved_photo_url: null,
    };
  },
  methods: {
    onFileSelected(event) {
      this.product_image = event.target.files[0];
      console.log(this.product_image);
      this.default_image_name = this.product_image.name;
    },
    submit_product() {
      if (
        this.chosen_category &&
        this.product_name &&
        this.product_price &&
        this.product_description
      ) {
        // We need to make sure we get the chosen_category id so
        console.log(this.product_image);
        let category_object = this.store_categories.find(
          (category) => category.name === this.chosen_category
        );

        // When uploading images we are going to use FormData Axios rather than our original way
        const fd = new FormData();
        fd.append("category", category_object.id);
        fd.append("name", this.product_name);
        fd.append("price", parseInt(this.product_price));
        fd.append("description", this.product_description);
        if (this.product_image) {
          fd.append("image", this.product_image);
        }
        axios({
          url: "admin_panel/post_product/",
          method: "POST",
          data: fd,
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
          .then((response) => {
            this.saved_photo_url = response.data.get_image;
            toast({
              message: `${this.product_name} was added to product list`,
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 6000, // milliseconds
              position: "bottom-right",
            });
            // We need to set show_added_product to true because we are going to need it to stay if we add a new one
            this.show_added_product = true;
          })
          .catch((err) => {
            console.log(err.response.data.name);
            this.error_message = err.response.data.name[0];
          });
      } else {
        this.error_message = "Please fill out the form";
      }
    },
    remove_file() {
      this.default_image_name = "No Files Selected";
      this.product_image = null;
    },
  },
  computed: {
    ...mapState(["store_categories", "accessToken"]),
  },
  created() {
    console.log(this.store_categories);
  },
};
</script>

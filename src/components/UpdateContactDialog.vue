<template>
  <v-dialog
    v-model="dialog"
    max-width="500"
  >
    <v-card
    >
      <v-card-title
        class="deep-purple accent-4"
      >
        <span >Update user form</span>
        
        <v-spacer></v-spacer>
        <v-btn 
          icon
          @click="dialog = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-title>
        <v-form 
          ref="form"
          v-model="valid"
          @submit.prevent="handleSubmit"
        >
          <v-text-field
            v-model="name"
            :rules="nameRules"
            :counter="20"
            label="Name"
            class="mt-5 mx-5"
            required
            filled
            color="deep-purple accent-2"
          ></v-text-field>

          <v-text-field
            v-model="phone"
            :rules="phoneRules"
            label="Phone"
            class="mx-5"
            required
            filled
            color="deep-purple accent-2"
          ></v-text-field>
            
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            class="mx-5"
            required
            filled
            color="deep-purple accent-2"
          ></v-text-field>

          <v-text-field
            v-model="image"
            label="Image"
            class="mx-5"
            filled
            color="deep-purple accent-2"
          ></v-text-field>

          <v-textarea
            v-model="desc"
            label="Description"
            class="mx-5"
            color="deep-purple accent-2"
            filled
            :rules="descRules"
            :counter="75"
          ></v-textarea>

            <v-divider></v-divider>

          <v-card-actions
            class="py-4"
          >
            <v-spacer></v-spacer>
            <v-btn 
              large 
            
              @click="dialog = false"
            >
              Close
            </v-btn>
            <v-btn 
              :loading="loading"
              :disabled="loading"
              large
              type="submit"
              color="deep-purple accent-4"
            >
              Update contact
            </v-btn>
            
          </v-card-actions>
        </v-form>
      <!-- </v-card-text> --> 
    </v-card>
  </v-dialog>
</template>

<script>
import { eventBus } from '../main';

export default {
  data: () => ({
    loading: false,
    dialog: false,
    valid: false,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => v.length >= 3 || 'Name must be more than 3 characters',
      v => v.length <= 20 || 'Name must be less than 20 characters'
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
    phone: '',
    phoneRules: [
      v => !!v || 'Phone is required',
      v => /^(\+7|8)\d{10}$/.test(v) || 'Phone must be valid'
    ], 
    desc: '',
    descRules: [
      v => v.length <= 75 || 'Description must be less than 75 characters'
    ],
    image: ''
  }),
  methods: {
    handleSubmit() {
      if (this.$refs.form.validate()) {
        this.loading = true;

        eventBus.$emit('edit', {
          action: 'update',
          data: {
            name: this.name,
            email: this.email,
            phone: this.phone,
            desc: this.desc,
            image: this.image
          },
          id: this.id
        })
      }
    },
  },
  created() {
    eventBus.$on('openUpdateDialog', data => {
      this.id = data.id;
      this.name = data.name;
      this.phone = data.phone;
      this.email = data.email;
      this.desc = data.desc;
      this.iamge = data.image;
      this.dialog = true;
    });

    eventBus.$on('updateResponse', () => {
      this.loading = false;
    })
  }
}
</script>
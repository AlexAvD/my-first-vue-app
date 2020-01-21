<template>
  <v-card
    elevation="5"
    tile
    height="100%"
    class="d-flex flex-column"
  >
    <v-toolbar 
        color="deep-purple accent-4 flex-grow-0"
        dense
        flat
      >
        <v-toolbar-title> 
          <span class="text-uppercase">
            {{name}}
          </span>
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn
          :loading="loading"
          :disabled="loading"
          icon
          @click="removeContact" 
          small
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-row 
        no-gutters
      >
        <v-col
          sm="12"
          lg="4"
        >
          <v-img
            :src="image || imagePlaceholder"
            :lazy-src="imagePlaceholder"
            height="100%"
            width="100%"
            max-width="100%"
            aspect-ratio="1"
          >
            <template v-slot:placeholder>
              <v-row
                class="fill-height ma-0" 
                align="center"
                justify="center"
              > 
                <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
              </v-row>
            </template>
            <v-card-actions class="align-end fill-height ">
              <v-btn
                :href="`tel:${phone}`"
                fab
                color="deep-purple accent-4"
              >
                 <v-icon>mdi-phone</v-icon>
              </v-btn>

              <v-spacer></v-spacer>

               <v-btn 
                small
                fab
                color="grey darken-3"
                @click="openUpdateDialog"
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>

            </v-card-actions>
          </v-img>
        </v-col>
        <v-col
          sm="12"
          lg="8"
          style="margin: auto 0;"
        >
          <v-list>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-phone</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{formattedPhone}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-divider 
              inset
            ></v-divider>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-email</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{email}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-divider 
              v-if="desc"
            ></v-divider>

            <v-list-item 
              three-line 
              v-if="desc"
            >
              <v-list-item-content>
                <v-list-item-title>About</v-list-item-title>
                <v-list-item-subtitle>
                  {{desc}}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
  </v-card>
</template>

<script>
import imagePlaceholder from '../assets/img/avatar-placeholder.gif';
import { eventBus } from '../main';

export default {
  data: () => ({
    loading: false,
    imagePlaceholder
  }),
  props: {
    id: String,
    name: String,
    phone: String,
    email: String,
    desc: String,
    image: String
  },
  computed: {
    formattedPhone() {
      return this.phone.replace(/(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})/, (match, a, b, c, d, e) => `+7 (${b}) ${c}-${d}-${e}`);
    }
  },
  methods: {
    removeContact() {
      this.loading = true;

      eventBus.$emit('edit', {
        action: 'delete',
        id: this.id
      });
    },
    openUpdateDialog() {
      eventBus.$emit('openUpdateDialog', this.$props);
    }
  },
  created() {
    eventBus.$on('removeResponse', () => {
      this.loading = false;
    })
  }
}
</script>
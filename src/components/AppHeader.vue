<template>
   <v-app-bar
      app
      color="deep-purple accent-4"
    >
      <v-toolbar-title>
        <span class="title ml-3 mr-5">Contact&nbsp;<span class="font-weight-light">App</span></span>
      </v-toolbar-title>

      <v-spacer></v-spacer>
      
      <v-text-field
        style="max-width: 350px;"
        class="ma-auto"
        placeholder="Search"
        append-icon="mdi-magnify"
        v-model="search"
        hide-details
        filled
        single-line
        rounded
        dense
        color="white" 
        @input="handleInput"
      ></v-text-field>
    </v-app-bar>
</template>

<script>
import { eventBus } from '../main'

export default {
  data: () => ({
    search: ''
  }),
  methods: {
    handleInput() {
      eventBus.$emit('search', this.search);
      // this.$emit('search', this.search);
    }
  }
}
</script>
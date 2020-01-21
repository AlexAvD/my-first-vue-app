<template>
  <v-container 
    class="pt-5"
    fill-height
  >
    <v-row 
      justify="center"
      style="width: 100%;"
    >
      <v-alert
        v-if="search !== '' && foundContacts.length === 0"
        color="deep-purple accent-4 font-weight-light headline px-5"
        elevation="5"
      >
        Contact not found.
      </v-alert>
      <v-col
          v-else
          v-for="contact in foundContacts"
          :key="contact.id"
          cols="12"
          sm="6"
          md="4"
          lg="6"
          xl="4"
        >
        <contact-card
          :id="contact.id"
          :name="contact.name"
          :phone="contact.phone"
          :email="contact.email"
          :desc="contact.desc"
          :image="contact.image"
        /> 
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContactCard from './ContactCard';

export default {
  props: {
    contacts: Array,
    search: String
  },
  components: {
    ContactCard
  },
  computed: {
    foundContacts() {
      if (this.search) {
        return this.contacts.filter(contact => contact.name.toLowerCase().indexOf(this.search.toLowerCase()) !== -1);
      }
      return this.contacts;
    }
  }
}
</script>
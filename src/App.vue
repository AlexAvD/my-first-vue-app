<template>
  <v-app>
    <app-header
    ></app-header>
    <app-content 
      :contacts="contacts" 
      :loading="loading"
      :search="search"
    ></app-content>
  </v-app>
</template>

<script>
import axios from 'axios';
import { eventBus } from './main';
import AppHeader from './components/AppHeader';
import AppContent from './components/AppContent';

export default {
  name: 'App',
  components: {
    AppHeader,
    AppContent,
  },
  methods: {
    editContact(data) {
      axios({
        method: 'POST',
        url: 'http://localhost:3000/api/contacts/edit', 
        data: JSON.stringify(data),
        headers: {
          'accept': ' application/json',
          'content-type': 'application/json'
        }
      })
      .then(resp => {
        const { action, result } = resp.data;
        
        switch (action) {
          case 'add': 
            this.addContact(result, data.data);
            break;
          case 'delete':
            this.removeContact(result);
            break;
          case 'update':
            this.updateContact(result, data.data);
            break;
          default:

            break;
        }
      })
      .catch(err => console.log(err));
    },
    addContact(result, data) {
      if (result) {
        this.contacts.push({
          id: result,
          ...data
        });
      }

      eventBus.$emit('addResponse');
    },
    removeContact(result) {
      if (result) {
        this.contacts = this.contacts.filter(contact => result !== contact.id);
      }

      eventBus.$emit('removeResponse');
    },
    updateContact(result, data) {
      if (result) {
        this.contacts = this.contacts.map(contact => {
          if (contact.id === result) {
            return {
              ...contact,
              ...data
            };
          }

          return contact;
        });
      }

      eventBus.$emit('updateResponse');
    }
  },
  created() {
    eventBus.$on('search', search => {
      this.search = search;
    });
    eventBus.$on('edit', data => {
      this.editContact(data);
    })
  },
  mounted() {
    axios.get('http://localhost:3000/api/contacts')
    .then(resp => {
      this.contacts = resp.data
      this.loading = false;
    })
  }, 
  data: () => ({
    contacts: [],
    search: '',
    loading: true
  })  
};
</script>

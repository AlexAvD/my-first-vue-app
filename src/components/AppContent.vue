<template>
    <v-content>
       <v-progress-linear
        :active="loading"
        :indeterminate="loading"
        absolute  
        top
        color="deep-purple"
      ></v-progress-linear> 
      <contact-list
        :contacts="contacts" 
        :search="search"
      />
      <add-contact-dialog></add-contact-dialog>
      <update-contact-dialog></update-contact-dialog>
    </v-content>
</template>

<script>
import ContactList from './ContactList'; 
import AddContactDialog from './AddContactDialog';
import UpdateContactDialog from './UpdateContactDialog';

export default {
  props: {
    contacts: Array,
    loading: Boolean,
    search: String
  },
  components: {
    ContactList,
    AddContactDialog,
    UpdateContactDialog
  }
}
</script>
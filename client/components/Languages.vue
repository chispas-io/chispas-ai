<template>
  <div class="hello">
    <h1>Random Fact:</h1>
    <button @click="fetchData">Click Me!</button>
    <p v-if="fact">{{ fact }}</p>
  </div>
</template>

<script>
export default {
  props: {
    msg: String,
  },
  data() {
    return {
      fact: "",
    };
  },
  methods: {
    fetchData() {
      fetch('/api/languages/list', {
        method: "GET",
        headers: {
          "Authorization-Token": 'XXXXXXXX',
        },
      })
          .then((response) => {
            response.json().then((data) => {
              console.log("LANGUAGES >>>", data);
              this.fact = data[0].fact;
            });
          })
          .catch((err) => {
            console.error(err);
          });
    },
  },
};
</script>
<style>
.hello {
  font-size: 2em;
  text-align: center;
}
</style>

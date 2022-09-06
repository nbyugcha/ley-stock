const { createApp } = Vue;

createApp({
  data() {
    return {
      resultado: '',
      data: {
        viscocidad: undefined,
        velocidad: undefined,
        api: undefined,
      },
    };
  },
  methods: {
    enviar() {
      this.resultado = ''
      fetch("/campo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.data),
      })
        .then((response) => response.json())
        .then((data) => {
          this.resultado = data.resultado
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
}).mount("#app");

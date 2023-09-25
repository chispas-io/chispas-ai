<template>
  <header class="bg-gray-50">
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <Logo />
        <div class="mt-4 text-center sm:text-left sm:mt-0">
          <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">
            Chispas
          </h1>

          <p class="mt-1.5 text-sm text-gray-500">
            Learn a language while having fun! 🎉
          </p>
        </div>
      </div>
    </div>
    <Nav />
  </header>
</template>

<script setup>
import Logo from './Logo.vue'
import Nav from "./Nav.vue";
</script>

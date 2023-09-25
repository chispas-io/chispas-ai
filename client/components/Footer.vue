<template>
  <footer class="bg-gray-50">
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <p class="text-center text-sm text-slate-900 font-medium lg:text-left">
          Chispas
        </p>
        <p class="mt-4 text-center text-sm text-gray-500 sm:mt-0 lg:text-right">
          Copyright &copy; {{ year }}. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

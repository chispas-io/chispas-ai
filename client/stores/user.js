import { defineStore } from "pinia";
import { jinxFetch } from "@/utils/api";

export const useUserStore = defineStore("user", {
    state: () => ({
        user: null,
    }),
    actions: {
        async fetchUser({ userToken }) {
            const res = await jinxFetch(`users/${userToken}`);

            const user = await res.json();
            this.user = user;
        },
        async signUp(email, password) {
            const res = await jinxFetch("account/register", {
                method: "POST",
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                body: JSON.stringify({ email, password }),
            });
            const user = await res.json()
            this.user = user;
        },
        async login(username, password) {
            const res = await jinxFetch("account/login", {
                method: "POST",
                headers: {
                    "Content-Type": "multipart/form-data",

                },
                body: new FormData({ username, password }),
            });
            const user = await res.json();
            console.log("USER >>>", user);
            this.user = user;
            // router.push("/"); // TODO: dont put router stuff in store
        },
        async authenticate(username, password) {
            const res = await jinxFetch(`account/authenticate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });
            const user = await res.json();
            console.log("USER >>>", user);
            this.user = user;
        },
        async logout() {
            const res = await jinxFetch("account/logout", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            this.user = null;
            // router.push("/login");
        },
    },
});

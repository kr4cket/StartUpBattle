import {createRouter, createWebHistory} from "vue-router";
import MainPage from "@/pages/MainPage.vue";
import LogInPage from "@/pages/LogInPage.vue";
import RegistrationPage from "@/pages/RegistrationPage.vue";

const routes = [
    {
        path: '/',
        component: MainPage,
    },
    {
        path: '/login',
        component: LogInPage,
    },
    {
        path: '/registration',
        component: RegistrationPage,
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
});

export default router;
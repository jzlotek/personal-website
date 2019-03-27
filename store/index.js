export const TOGGLE_NAV = 'TOGGLE_NAV';
export const NAV_VISIBLE = 'NAV_VISIBLE';

export const state = () => ({
    NAV_VISIBLE: false,
})

export const mutations = {
    [TOGGLE_NAV](state) {
        state.NAV_VISIBLE = !state.NAV_VISIBLE;
    },
}

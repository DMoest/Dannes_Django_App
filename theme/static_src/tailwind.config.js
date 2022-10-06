/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    100: 'var(--color-primary-100)',
                    200: 'var(--color-primary-200)',
                    300: 'var(--color-primary-300)',
                    400: 'var(--color-primary-400)',
                    500: 'var(--color-primary-500)',
                },
                secondary: {
                    100: 'var(--color-secondary-100)',
                    200: 'var(--color-secondary-200)',
                    300: 'var(--color-secondary-300)',
                    400: 'var(--color-secondary-400)',
                    500: 'var(--color-secondary-500)',
                },
                tertiary: {
                    100: 'var(--color-tertiary-100)',
                    200: 'var(--color-tertiary-200)',
                    300: 'var(--color-tertiary-300)',
                    400: 'var(--color-tertiary-400)',
                    500: 'var(--color-tertiary-500)',
                },
                quaternary: {
                    100: 'var(--color-quaternary-100)',
                    200: 'var(--color-quaternary-200)',
                    300: 'var(--color-quaternary-300)',
                    400: 'var(--color-quaternary-400)',
                    500: 'var(--color-quaternary-500)',
                },
                quinary: {
                    100: 'var(--color-quinary-100)',
                    200: 'var(--color-quinary-200)',
                    300: 'var(--color-quinary-300)',
                    400: 'var(--color-quinary-400)',
                    500: 'var(--color-quinary-500)',
                },
                response: {
                    info: 'var(--color-info)',
                    success: 'var(--color-success)',
                    caution: 'var(--color-caution)',
                    warning: 'var(--color-warning)',
                    danger: 'var(--color-danger)',
                },
                social: {
                    bitbucket: 'var(--color-social-bitbucket)',
                    discord: 'var(--color-social-discord)',
                    facebook: 'var(--color-social-facebook)',
                    flickr: 'var(--color-social-flickr)',
                    github: 'var(--color-social-github)',
                    gitlab: 'var(--color-social-gitlab)',
                    instagram: 'var(--color-social-instagram)',
                    linkedin: 'var(--color-social-linkedin)',
                    pinterest: 'var(--color-social-pinterest)',
                    reddit: 'var(--color-social-reddit)',
                    skype: 'var(--color-social-skype)',
                    spotify: 'var(--color-social-spotify)',
                    slack: 'var(--color-social-slack)',
                    snapchat: 'var(--color-social-snapchat)',
                    soundcloud: 'var(--color-social-soundcloud)',
                    stackoverflow: 'var(--color-social-stackoverflow)',
                    telegram: 'var(--color-social-telegram)',
                    twitch: 'var(--color-social-twitch)',
                    twitter: 'var(--color-social-twitter)',
                    tumblr: 'var(--color-social-tumblr)',
                    vimeo: 'var(--color-social-vimeo)',
                    whatsapp: 'var(--color-social-whatsapp)',
                    yahoo: 'var(--color-social-yahoo)',
                    youtube: 'var(--color-social-youtube)',
                },
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}

/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDocsConfig from "../../..";

export interface DocsInstances {
    url: string;
    customDomain?: FernDocsConfig.CustomDomain;
    audiences?: FernDocsConfig.AudiencesConfig;
    /** If `private` is set to true, Fern will protect the docs site with SSO. */
    private?: boolean;
    /** If `edit-this-page` is set, Fern will add an "Edit this page" link to the bottom of each page that links to the given GitHub repository. */
    editThisPage?: FernDocsConfig.EditThisPageConfig;
}

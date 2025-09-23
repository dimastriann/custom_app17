/** @odoo-module **/

import {CharField, charField} from "@web/views/fields/char/char_field";
import {onMounted} from "@odoo/owl";
import {registry} from "@web/core/registry";


export class InputCharMask extends CharField {
    setup() {
        super.setup();
        onMounted(this.onMounted);
    }

    onMounted() {
        const maskOptions = {
            mask: this.props.maskType,
            lazy: false,
        };
        IMask(this.input.el, maskOptions);
    }

    parse(value) {
        return value && value.replace(/\D/g, "");
    }
}

InputCharMask.template = "input_mask_widget.CharMask";
InputCharMask.props = {
    ...CharField.props,
    maskType: {type: String, optional: true},
}
InputCharMask.defaultProps = {
    ...CharField.defaultProps,
    maskType: "000-000-000-000"
}
export const inputCharMask = {
    ...charField,
    component: InputCharMask,
    extractProps: ({attrs}) => ({
        maskType: attrs.data_mask_type,
    })
}

registry.category("fields").add("char_mask", inputCharMask);

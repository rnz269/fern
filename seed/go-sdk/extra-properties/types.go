// This file was auto-generated by Fern from our API Definition.

package extraproperties

import (
	json "encoding/json"
	fmt "fmt"
	core "github.com/extra-properties/fern/core"
)

type Failure struct {
	status string

	ExtraProperties map[string]interface{} `json:"-" url:"-"`

	_rawJSON json.RawMessage
}

func (f *Failure) Status() string {
	return f.status
}

func (f *Failure) UnmarshalJSON(data []byte) error {
	type embed Failure
	var unmarshaler = struct {
		embed
	}{
		embed: embed(*f),
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	*f = Failure(unmarshaler.embed)
	f.status = "failure"

	extraProperties, err := core.ExtractExtraProperties(data, *f, "status")
	if err != nil {
		return err
	}
	f.ExtraProperties = extraProperties

	f._rawJSON = json.RawMessage(data)
	return nil
}

func (f *Failure) MarshalJSON() ([]byte, error) {
	type embed Failure
	var marshaler = struct {
		embed
		Status string `json:"status"`
	}{
		embed:  embed(*f),
		Status: "failure",
	}
	return core.MarshalJSONWithExtraProperties(marshaler, f.ExtraProperties)
}

func (f *Failure) String() string {
	if len(f._rawJSON) > 0 {
		if value, err := core.StringifyJSON(f._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(f); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", f)
}

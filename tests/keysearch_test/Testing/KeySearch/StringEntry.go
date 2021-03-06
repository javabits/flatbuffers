// automatically generated by the FlatBuffers compiler, do not modify

package KeySearch

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type StringEntry struct {
	_tab flatbuffers.Table
}

func GetRootAsStringEntry(buf []byte, offset flatbuffers.UOffsetT) *StringEntry {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &StringEntry{}
	x.Init(buf, n+offset)
	return x
}

func (rcv *StringEntry) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *StringEntry) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *StringEntry) Key() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func (rcv *StringEntry) Value() int32 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.GetInt32(o + rcv._tab.Pos)
	}
	return 7890
}

func (rcv *StringEntry) MutateValue(n int32) bool {
	return rcv._tab.MutateInt32Slot(6, n)
}

func StringEntryStart(builder *flatbuffers.Builder) {
	builder.StartObject(2)
}
func StringEntryAddKey(builder *flatbuffers.Builder, key flatbuffers.UOffsetT) {
	builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(key), 0)
}
func StringEntryAddValue(builder *flatbuffers.Builder, value int32) {
	builder.PrependInt32Slot(1, value, 7890)
}
func StringEntryEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}

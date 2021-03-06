<?php
// automatically generated by the FlatBuffers compiler, do not modify

namespace Testing\KeySearch;

use \Google\FlatBuffers\Struct;
use \Google\FlatBuffers\Table;
use \Google\FlatBuffers\ByteBuffer;
use \Google\FlatBuffers\FlatBufferBuilder;

class BoolEntry extends Table
{
    /**
     * @param ByteBuffer $bb
     * @return BoolEntry
     */
    public static function getRootAsBoolEntry(ByteBuffer $bb)
    {
        $obj = new BoolEntry();
        return ($obj->init($bb->getInt($bb->getPosition()) + $bb->getPosition(), $bb));
    }

    public static function BoolEntryIdentifier()
    {
        return "FBMD";
    }

    public static function BoolEntryBufferHasIdentifier(ByteBuffer $buf)
    {
        return self::__has_identifier($buf, self::BoolEntryIdentifier());
    }

    public static function BoolEntryExtension()
    {
        return "mdict";
    }

    /**
     * @param int $_i offset
     * @param ByteBuffer $_bb
     * @return BoolEntry
     **/
    public function init($_i, ByteBuffer $_bb)
    {
        $this->bb_pos = $_i;
        $this->bb = $_bb;
        return $this;
    }

    /**
     * @return bool
     */
    public function getKey()
    {
        $o = $this->__offset(4);
        return $o != 0 ? $this->bb->getBool($o + $this->bb_pos) : false;
    }

    /**
     * @return bool
     */
    public function getValue()
    {
        $o = $this->__offset(6);
        return $o != 0 ? $this->bb->getBool($o + $this->bb_pos) : true;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return void
     */
    public static function startBoolEntry(FlatBufferBuilder $builder)
    {
        $builder->StartObject(2);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return BoolEntry
     */
    public static function createBoolEntry(FlatBufferBuilder $builder, $key, $value)
    {
        $builder->startObject(2);
        self::addKey($builder, $key);
        self::addValue($builder, $value);
        $o = $builder->endObject();
        return $o;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param bool
     * @return void
     */
    public static function addKey(FlatBufferBuilder $builder, $key)
    {
        $builder->addBoolX(0, $key, false);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param bool
     * @return void
     */
    public static function addValue(FlatBufferBuilder $builder, $value)
    {
        $builder->addBoolX(1, $value, false);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return int table offset
     */
    public static function endBoolEntry(FlatBufferBuilder $builder)
    {
        $o = $builder->endObject();
        return $o;
    }
}

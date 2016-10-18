<?php
// automatically generated by the FlatBuffers compiler, do not modify

namespace Testing\KeySearch;

use \Google\FlatBuffers\Struct;
use \Google\FlatBuffers\Table;
use \Google\FlatBuffers\ByteBuffer;
use \Google\FlatBuffers\FlatBufferBuilder;

class FloatEntry extends Table
{
    /**
     * @param ByteBuffer $bb
     * @return FloatEntry
     */
    public static function getRootAsFloatEntry(ByteBuffer $bb)
    {
        $obj = new FloatEntry();
        return ($obj->init($bb->getInt($bb->getPosition()) + $bb->getPosition(), $bb));
    }

    public static function FloatEntryIdentifier()
    {
        return "FBMD";
    }

    public static function FloatEntryBufferHasIdentifier(ByteBuffer $buf)
    {
        return self::__has_identifier($buf, self::FloatEntryIdentifier());
    }

    public static function FloatEntryExtension()
    {
        return "mdict";
    }

    /**
     * @param int $_i offset
     * @param ByteBuffer $_bb
     * @return FloatEntry
     **/
    public function init($_i, ByteBuffer $_bb)
    {
        $this->bb_pos = $_i;
        $this->bb = $_bb;
        return $this;
    }

    /**
     * @return float
     */
    public function getKey()
    {
        $o = $this->__offset(4);
        return $o != 0 ? $this->bb->getFloat($o + $this->bb_pos) : 0.0;
    }

    /**
     * @return float
     */
    public function getValue()
    {
        $o = $this->__offset(6);
        return $o != 0 ? $this->bb->getFloat($o + $this->bb_pos) : 1234.0;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return void
     */
    public static function startFloatEntry(FlatBufferBuilder $builder)
    {
        $builder->StartObject(2);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return FloatEntry
     */
    public static function createFloatEntry(FlatBufferBuilder $builder, $key, $value)
    {
        $builder->startObject(2);
        self::addKey($builder, $key);
        self::addValue($builder, $value);
        $o = $builder->endObject();
        return $o;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param float
     * @return void
     */
    public static function addKey(FlatBufferBuilder $builder, $key)
    {
        $builder->addFloatX(0, $key, 0.0);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param float
     * @return void
     */
    public static function addValue(FlatBufferBuilder $builder, $value)
    {
        $builder->addFloatX(1, $value, 1234.0);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return int table offset
     */
    public static function endFloatEntry(FlatBufferBuilder $builder)
    {
        $o = $builder->endObject();
        return $o;
    }
}

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        '''Metiendo todos los datos del campo anterior a
        modelo'''
        for unidad in orm.UnidadProducto.objects.all():
            unidad_int = orm.UnidadInternacional(nombre=unidad.unidad_int)
            try:
                unidad_int.save()
            except:
                print 'repetido ', unidad.unidad_int


    def backwards(self, orm):
        "Write your backwards methods here."
        pass


    models = {
        'diversity.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"})
        },
        'diversity.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo_int': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'precio.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'precio.precio': {
            'Meta': {'object_name': 'Precio'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Moneda']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio_productor': ('django.db.models.fields.FloatField', [], {}),
            'precios2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Precios']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'precio.precioconsumidor': {
            'Meta': {'object_name': 'PrecioConsumidor'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Moneda']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Pais']"}),
            'precio_consumidor': ('django.db.models.fields.FloatField', [], {}),
            'precios1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Precios']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Producto']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.UnidadProducto']"}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diversity.Lugar']"})
        },
        'precio.precios': {
            'Meta': {'object_name': 'Precios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'precio.producto': {
            'Meta': {'object_name': 'Producto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'precio.tipocambio': {
            'Meta': {'unique_together': "(['moneda_local', 'moneda_extranjera', 'fecha'],)", 'object_name': 'TipoCambio'},
            'cantidad_extranjera': ('django.db.models.fields.FloatField', [], {}),
            'cantidad_local': ('django.db.models.fields.FloatField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda_extranjera': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipocambio_moneda'", 'to': "orm['precio.Moneda']"}),
            'moneda_local': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precio.Moneda']"})
        },
        'precio.unidadinternacional': {
            'Meta': {'object_name': 'UnidadInternacional'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'precio.unidadproducto': {
            'Meta': {'object_name': 'UnidadProducto'},
            'equivalente': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad_int': ('django.db.models.fields.CharField', [], {'max_length': "10"})
        },
        'precio.variedad': {
            'Meta': {'object_name': 'Variedad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['precio']

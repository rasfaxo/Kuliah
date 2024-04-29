import 'package:flutter/material.dart';

class ProdukForm extends StatefulWidget {
  const ProdukForm({super.key});
  @override
  // ignore: library_private_types_in_public_api
  _ProdukFormState createState() => _ProdukFormState();
}

class _ProdukFormState extends State<ProdukForm> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Produk Form'),
        ),
        body: SingleChildScrollView(
          child: Column(
            children: [
              const TextField(
                decoration: InputDecoration(labelText: "Kode Produk"),
              ),
              const TextField(
                decoration: InputDecoration(labelText: "Nama Produk"),
              ),
              const TextField(
                decoration: InputDecoration(labelText: "Harga"),
              ),
              ElevatedButton(child: const Text("simpan"), onPressed: () {}),
            ],
          ),
        ));
  }
}

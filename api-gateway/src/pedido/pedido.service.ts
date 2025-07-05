import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class PedidoService {
  private baseUrl = 'http://localhost:8000/pedidos'; // URL microservicio Python

  async findAll() {
    try {
      const { data } = await axios.get(this.baseUrl);
      return data;
    } catch (error) {
      throw new HttpException('Error fetching pedidos', HttpStatus.BAD_GATEWAY);
    }
  }

  async findOne(id: number) {
    try {
      const { data } = await axios.get(`${this.baseUrl}/${id}`);
      return data;
    } catch (error) {
      throw new HttpException('Pedido not found', HttpStatus.NOT_FOUND);
    }
  }
}

import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class OfertaService {
  private baseUrl = 'http://localhost:3001/ofertas'; // Cambia esta URL por la de tu microservicio ofertas

  async findAll() {
    try {
      const { data } = await axios.get(this.baseUrl);
      return data;
    } catch (error) {
      throw new HttpException('Error fetching ofertas', HttpStatus.BAD_GATEWAY);
    }
  }

  async findOne(id: number) {
    try {
      const { data } = await axios.get(`${this.baseUrl}/${id}`);
      return data;
    } catch (error) {
      throw new HttpException('Oferta not found', HttpStatus.NOT_FOUND);
    }
  }
}

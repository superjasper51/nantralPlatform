import axios from 'axios';

import { adaptApiErrors, ApiErrorDTO } from '#shared/infra/errors';
import { adaptPage } from '#shared/infra/pagination';

import { adaptShortcut } from '../infra/shortcut.adapter';

interface ShortcutListQueryParams {
  page?: number;
  pageSize?: number;
}

export async function getShortcutListApi(params: ShortcutListQueryParams) {
  const { data } = await axios
    .get('api/shortcut/', { params: params })
    .catch((errors: ApiErrorDTO) => {
      throw adaptApiErrors(errors);
    });
  return adaptPage(data, adaptShortcut);
}
